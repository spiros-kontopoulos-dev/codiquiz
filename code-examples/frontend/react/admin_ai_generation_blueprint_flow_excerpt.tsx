// Selected sanitized excerpt from Codiquiz AdminAiGenerationCreatePage.
// Shows how ranked Blueprint candidates become editable AI generation plan rows.
// This is a partial excerpt and is not intended to compile standalone.

function hasBlueprintPriorityMetadata(item: AiGenerationPlanItemPreview) {
  return item.blueprint_generation_priority_score !== undefined;
}

function clearBlueprintPriorityMetadata(
  item: AiGenerationPlanItemPreview,
): AiGenerationPlanItemPreview {
  return {
    ...item,
    blueprint_generation_priority_score: null,
    blueprint_generation_priority_bucket: null,
    blueprint_generation_priority_reasons: [],
    blueprint_suitability_score: null,
    blueprint_suitability_tier: null,
    blueprint_target_count: null,
    blueprint_hard_gap_count: null,
    blueprint_effective_gap_count: null,
    blueprint_pending_review_count: null,
    blueprint_rule_id: null,
    blueprint_rule_scope_key: null,
    blueprint_metadata_source: null,
  };
}

function blueprintPriorityMetadataFromCoverageRow(
  row: BlueprintCoverageRow,
  source: "blueprint_candidate" | "blueprint_lookup",
): BlueprintPriorityMetadata {
  return {
    blueprint_generation_priority_score: row.generation_priority_score,
    blueprint_generation_priority_bucket: row.generation_priority_bucket,
    blueprint_generation_priority_reasons: row.generation_priority_reasons,
    blueprint_suitability_score: row.suitability_score,
    blueprint_suitability_tier: row.suitability_tier,
    blueprint_target_count: row.target_count,
    blueprint_hard_gap_count: row.hard_gap_count,
    blueprint_effective_gap_count: row.effective_gap_count,
    blueprint_pending_review_count: row.pending_review_count,
    blueprint_rule_id: row.rule_id,
    blueprint_rule_scope_key: row.rule_scope_key,
    blueprint_metadata_source: source,
  };
}

function blueprintPriorityMetadataFromCandidate(
  candidate: BlueprintGenerationCandidate,
): BlueprintPriorityMetadata {
  return {
    blueprint_generation_priority_score: candidate.generation_priority_score,
    blueprint_generation_priority_bucket: candidate.generation_priority_bucket,
    blueprint_generation_priority_reasons: candidate.generation_priority_reasons,
    blueprint_suitability_score: candidate.suitability_score,
    blueprint_suitability_tier: candidate.suitability_tier,
    blueprint_target_count: candidate.target_count,
    blueprint_hard_gap_count: candidate.hard_gap_count,
    blueprint_effective_gap_count: candidate.effective_gap_count,
    blueprint_pending_review_count: candidate.pending_review_count,
    blueprint_rule_id: candidate.rule_id,
    blueprint_rule_scope_key: candidate.rule_scope_key,
    blueprint_metadata_source: "blueprint_candidate",
  };
}

function blueprintPriorityLookupKey(item: AiGenerationPlanItemPreview) {
  if (
    item.technology_id === null ||
    item.technology_domain_id === null ||
    item.technology_module_id === null ||
    item.technology_topic_id === null ||
    item.primary_concept_id === null ||
    item.question_type_id === null ||
    !isBlueprintDifficulty(item.difficulty)
  ) {
    return null;
  }

  return [
    item.technology_id,
    item.technology_domain_id,
    item.technology_module_id,
    item.technology_topic_id,
    item.technology_subtopic_id ?? "",
    item.primary_concept_id,
    item.question_type_id,
    item.difficulty,
  ].join(":");
}

async function fetchBlueprintPriorityMetadataForItem(
  item: AiGenerationPlanItemPreview,
): Promise<BlueprintPriorityMetadata | null> {
  if (
    item.technology_id === null ||
    item.technology_domain_id === null ||
    item.technology_module_id === null ||
    item.technology_topic_id === null ||
    item.primary_concept_id === null ||
    item.question_type_id === null ||
    !isBlueprintDifficulty(item.difficulty)
  ) {
    return null;
  }

  try {
    const response = await fetchBlueprintCoverage({
      page: 1,
      pageSize: 1,
      onlyGaps: false,
      technologyId: item.technology_id,
      technologyDomainId: item.technology_domain_id,
      technologyModuleId: item.technology_module_id,
      technologyTopicId: item.technology_topic_id,
      technologySubtopicId: item.technology_subtopic_id,
      conceptId: item.primary_concept_id,
      questionTypeId: item.question_type_id,
      difficulty: item.difficulty,
      coverageStatus: "all",
      suitabilityTier: "all",
      sortBy: "generation_priority",
      sortDir: "desc",
    });

    const row = response.rows[0];
    return row ? blueprintPriorityMetadataFromCoverageRow(row, "blueprint_lookup") : null;
  } catch {
    // Blueprint priority is helpful context, but previewing a manual plan should
    // still work if the lookup fails or the exact cell is not in the Blueprint.
    return null;
  }
}

async function enrichPreviewItemsWithBlueprintPriority(
  items: AiGenerationPlanItemPreview[],
): Promise<AiGenerationPlanItemPreview[]> {
  const lookupItemsByKey = new Map<string, AiGenerationPlanItemPreview>();

  items.forEach((item) => {
    if (hasBlueprintPriorityMetadata(item)) {
      return;
    }

    const key = blueprintPriorityLookupKey(item);
    if (key && lookupItemsByKey.size < MAX_BLUEPRINT_PRIORITY_LOOKUPS) {
      lookupItemsByKey.set(key, item);
    }
  });

  if (lookupItemsByKey.size === 0) {
    return items;
  }

  const metadataEntries = await Promise.all(
    Array.from(lookupItemsByKey.entries()).map(async ([key, item]) => [
      key,
      await fetchBlueprintPriorityMetadataForItem(item),
    ] as const),
  );
  const metadataByKey = new Map(metadataEntries);

  return items.map((item) => {
    const key = blueprintPriorityLookupKey(item);
    const metadata = key ? metadataByKey.get(key) : null;

    return metadata ? { ...item, ...metadata } : clearBlueprintPriorityMetadata(item);
  });
}

function blueprintCandidateToPreviewItem(
  candidate: BlueprintGenerationCandidate,
  position: number,
): AiGenerationPlanItemPreview {
  const planItem = candidate.plan_item;

  return {
    position,
    requested_count: planItem.requested_count,
    generation_mode: planItem.generation_mode,
    language_id: null,
    language_name: null,
    category_id: null,
    category_name: null,
    topic_id: null,
    topic_name: null,
    technology_id: planItem.technology_id,
    technology_name: candidate.path.technology?.name ?? null,
    technology_domain_id: planItem.technology_domain_id,
    technology_domain_name: candidate.path.domain?.name ?? null,
    technology_module_id: planItem.technology_module_id,
    technology_module_name: candidate.path.module?.name ?? null,
    technology_topic_id: planItem.technology_topic_id,
    technology_topic_name: candidate.path.topic?.name ?? null,
    technology_subtopic_id: nullableNumberValue(planItem.technology_subtopic_id),
    technology_subtopic_name: candidate.path.subtopic?.name ?? null,
    primary_concept_id: planItem.primary_concept_id,
    primary_concept_name: candidate.concept_name,
    question_type_id: planItem.question_type_id,
    question_type_name: candidate.question_type_name,
    difficulty: planItem.difficulty,
    prompt_context: planItem.prompt_context,
    ...blueprintPriorityMetadataFromCandidate(candidate),
  };
}

function blueprintCandidatesToPlanPreview(
  response: BlueprintGenerationCandidatesResponse,
): AiGenerationPlanPreview {
  const planItems = response.candidates.map((candidate, index) =>
    blueprintCandidateToPreviewItem(candidate, index + 1),
  );

  return {
    requested_count: response.requested_count,
    planned_count: sumPlanItemCounts(planItems),
    generation_mode: response.generation_mode,
    plan_item_count: planItems.length,
    allocation_strategy: response.allocation_strategy,
    plan_items: planItems,
  };
}

function reindexPlanPreviewItems(
  items: AiGenerationPlanItemPreview[],
): AiGenerationPlanItemPreview[] {
  return items.map((item, index) => ({
    ...item,
    position: index + 1,
  }));
}

type BlueprintAppendResult = {
  preview: AiGenerationPlanPreview;
  appendedCount: number;
  skippedDuplicateCount: number;
};

function appendBlueprintCandidatesToPreview(
  currentPreview: AiGenerationPlanPreview,
  currentItems: AiGenerationPlanItemPreview[],
  incomingPreview: AiGenerationPlanPreview,
): BlueprintAppendResult {
  const existingTargetKeys = new Set(
    currentItems.map((item) => planItemTargetKey(item)),
  );
  const appendedItems = incomingPreview.plan_items.filter(
    (item) => !existingTargetKeys.has(planItemTargetKey(item)),
  );
  const skippedDuplicateCount =
    incomingPreview.plan_items.length - appendedItems.length;
  const mergedItems = reindexPlanPreviewItems([...currentItems, ...appendedItems]);

  return {
    preview: {
      ...incomingPreview,
      requested_count: sumPlanItemCounts(mergedItems),
      planned_count: sumPlanItemCounts(mergedItems),
      generation_mode: currentPreview.generation_mode,
      plan_item_count: mergedItems.length,
      allocation_strategy: "manual",
      plan_items: mergedItems,
    },
    appendedCount: appendedItems.length,
    skippedDuplicateCount,
  };
}

function planPreviewItemToInput(
  item: AiGenerationPlanItemPreview,
): AiGenerationPlanItemInput {
  return {
    requested_count: item.requested_count,
    generation_mode: item.generation_mode,
    language_id: item.language_id,
    category_id: item.category_id,
    topic_id: item.topic_id,
    technology_id: item.technology_id,
    technology_domain_id: item.technology_domain_id,
    technology_module_id: item.technology_module_id,
    technology_topic_id: item.technology_topic_id,
