// Blueprint coverage/candidate TypeScript models
// Source: frontend/src/api/adminBlueprintCoverage.ts (excerpt lines 47-145)
// Public portfolio excerpt; not standalone application code.

export type BlueprintCoverageSortDirection = "asc" | "desc";

export type BlueprintCoveragePathNode = {
  id: number;
  slug: string;
  name: string;
};

export type BlueprintCoveragePath = {
  field: BlueprintCoveragePathNode | null;
  technology: BlueprintCoveragePathNode | null;
  domain: BlueprintCoveragePathNode | null;
  module: BlueprintCoveragePathNode | null;
  topic: BlueprintCoveragePathNode | null;
  subtopic: BlueprintCoveragePathNode | null;
  concept: BlueprintCoveragePathNode | null;
};

export type BlueprintCoverageSummary = {
  include_inactive: boolean;
  active_rule_count: number;
  total_blueprint_cells: number;
  total_target_questions: number;
  approved_questions_counted: number;
  pending_review_ai_questions_counted: number;
  hard_gap_count: number;
  effective_gap_count: number;
  covered_cells: number;
  hard_gap_cells: number;
  effective_gap_cells: number;
  all_eligible_cells: number;
  recommended_target_cells: number;
  recommended_gap_cells: number;
  strong_fit_cells: number;
  strong_fit_gap_cells: number;
  secondary_fit_cells: number;
  secondary_fit_gap_cells: number;
  weak_manual_cells: number;
  unrated_review_cells: number;
  excluded_cells: number;
};

export type BlueprintCoveragePage = {
  page: number;
  page_size: number;
  total_count: number;
  only_gaps: boolean;
  technology_id: number | null;
  technology_domain_id: number | null;
  technology_module_id: number | null;
  technology_topic_id: number | null;
  technology_subtopic_id: number | null;
  concept_id: number | null;
  question_type_id: number | null;
  difficulty: BlueprintCoverageDifficulty | null;
  search: string | null;
  coverage_status: BlueprintCoverageStatusFilter;
  suitability_tier: BlueprintSuitabilityTierFilter;
  sort_by: BlueprintCoverageSortBy;
  sort_dir: BlueprintCoverageSortDirection;
};

export type BlueprintCoverageRow = {
  concept_id: number;
  concept_slug: string;
  concept_name: string;
  path: BlueprintCoveragePath;
  question_type_id: number;
  question_type_code: string;
  question_type_name: string;
  difficulty: BlueprintCoverageDifficulty;
  suitability_score: number | null;
  suitability_base_score: number | null;
  suitability_difficulty_weight: number;
  suitability_source_level: string | null;
  suitability_source_key: string | null;
  suitability_source_name: string | null;
  suitability_rule_id: number | null;
  suitability_tier: BlueprintSuitabilityTier;
  suitability_target_mode: BlueprintSuitabilityTargetMode;
  blueprint_rule_target_count: number;
  target_count: number;
  approved_count: number;
  pending_review_count: number;
  hard_gap_count: number;
  effective_gap_count: number;
  coverage_pct: number;
  effective_coverage_pct: number;
  generation_priority_score: number;
  generation_priority_bucket: BlueprintGenerationPriorityBucket;
  generation_priority_reasons: string[];
  rule_id: number;
  rule_scope_key: string;
  rule_scope_level: string;
  rule_priority: number;
  rule_source: string;
  rule_notes: string | null;
};


// Blueprint coverage client call
// Source: frontend/src/api/adminBlueprintCoverage.ts (excerpt lines 306-389)
// Public portfolio excerpt; not standalone application code.

export async function fetchBlueprintCoverage(
  options: FetchBlueprintCoverageOptions = {},
): Promise<BlueprintCoverageResponse> {
  const searchParams = new URLSearchParams();

  searchParams.set("page", String(options.page ?? 1));
  searchParams.set("page_size", String(options.pageSize ?? 20));
  searchParams.set("only_gaps", String(options.onlyGaps ?? true));

  setNumericParam(searchParams, "technology_id", options.technologyId);
  setNumericParam(
    searchParams,
    "technology_domain_id",
    options.technologyDomainId,
  );
  setNumericParam(
    searchParams,
    "technology_module_id",
    options.technologyModuleId,
  );
  setNumericParam(
    searchParams,
    "technology_topic_id",
    options.technologyTopicId,
  );
  setNumericParam(
    searchParams,
    "technology_subtopic_id",
    options.technologySubtopicId,
  );
  setNumericParam(searchParams, "concept_id", options.conceptId);
  setNumericParam(searchParams, "question_type_id", options.questionTypeId);

  if (options.difficulty) {
    searchParams.set("difficulty", options.difficulty);
  }

  const search = options.search?.trim();
  if (search) {
    searchParams.set("search", search);
  }

  searchParams.set("coverage_status", options.coverageStatus ?? "all");
  searchParams.set("suitability_tier", options.suitabilityTier ?? "recommended");
  searchParams.set("sort_by", options.sortBy ?? "generation_priority");
  searchParams.set("sort_dir", options.sortDir ?? "desc");

  const response = await adminFetch(
    `${API_URL}/admin/blueprint/coverage?${searchParams.toString()}`,
  );

  if (!response.ok) {
    throw new Error(
      await readErrorMessage(response, "Failed to fetch blueprint coverage"),
    );
  }

  return response.json();
}

export async function fetchBlueprintDefaultTargets(
  options: FetchBlueprintDefaultTargetsOptions = {},
): Promise<BlueprintDefaultTargetsResponse> {
  const searchParams = new URLSearchParams();

  searchParams.set("page", String(options.page ?? 1));
  searchParams.set("page_size", String(options.pageSize ?? 20));
  searchParams.set("only_gaps", String(options.onlyGaps ?? true));

  setNumericParam(searchParams, "technology_id", options.technologyId);
  setNumericParam(
    searchParams,
    "technology_domain_id",
    options.technologyDomainId,
  );
  setNumericParam(
    searchParams,
    "technology_module_id",
    options.technologyModuleId,
  );
  setNumericParam(
    searchParams,
    "technology_topic_id",
    options.technologyTopicId,

// Blueprint generation candidate client call
// Source: frontend/src/api/adminBlueprintCoverage.ts (excerpt lines 430-566)
// Public portfolio excerpt; not standalone application code.

export type BlueprintGenerationCandidatePlanItem = {
  requested_count: number;
  generation_mode: "normal" | "reverse";
  technology_id: number;
  technology_domain_id: number;
  technology_module_id: number;
  technology_topic_id: number;
  technology_subtopic_id: number | null;
  primary_concept_id: number;
  question_type_id: number;
  difficulty: BlueprintCoverageDifficulty;
  prompt_context: string | null;
};

export type BlueprintGenerationCandidate = {
  rank: number;
  requested_count: number;
  concept_id: number;
  concept_slug: string;
  concept_name: string;
  path: BlueprintCoveragePath;
  question_type_id: number;
  question_type_code: string;
  question_type_name: string;
  difficulty: BlueprintCoverageDifficulty;
  target_count: number;
  approved_count: number;
  pending_review_count: number;
  hard_gap_count: number;
  effective_gap_count: number;
  suitability_score: number | null;
  suitability_tier: BlueprintSuitabilityTier;
  generation_priority_score: number;
  generation_priority_bucket: BlueprintGenerationPriorityBucket;
  generation_priority_reasons: string[];
  rule_id: number;
  rule_scope_key: string;
  rule_priority: number;
  plan_item: BlueprintGenerationCandidatePlanItem;
};

export type BlueprintGenerationCandidatesPage = {
  page: number;
  page_size: number;
  total_count: number;
};

export type BlueprintGenerationCandidatesResponse = {
  total_candidate_count: number;
  page: BlueprintGenerationCandidatesPage;
  returned_candidate_count: number;
  requested_count: number;
  generation_mode: "normal";
  allocation_strategy: "manual";
  max_questions_per_candidate: number;
  candidates: BlueprintGenerationCandidate[];
  plan_items: BlueprintGenerationCandidatePlanItem[];
};

export type FetchBlueprintGenerationCandidatesOptions = {
  page?: number;
  pageSize?: number;
  maxQuestionsPerCandidate?: number;
  technologyId?: number | null;
  technologyDomainId?: number | null;
  technologyModuleId?: number | null;
  technologyTopicId?: number | null;
  technologySubtopicId?: number | null;
  conceptId?: number | null;
  questionTypeId?: number | null;
  difficulty?: BlueprintCoverageDifficulty | null;
  search?: string | null;
  suitabilityTier?: BlueprintSuitabilityTierFilter;
};

export async function fetchBlueprintGenerationCandidates(
  options: FetchBlueprintGenerationCandidatesOptions = {},
): Promise<BlueprintGenerationCandidatesResponse> {
  const searchParams = new URLSearchParams();

  searchParams.set("page", String(options.page ?? 1));
  searchParams.set("page_size", String(options.pageSize ?? 10));
  searchParams.set(
    "max_questions_per_candidate",
    String(options.maxQuestionsPerCandidate ?? 5),
  );

  setNumericParam(searchParams, "technology_id", options.technologyId);
  setNumericParam(
    searchParams,
    "technology_domain_id",
    options.technologyDomainId,
  );
  setNumericParam(
    searchParams,
    "technology_module_id",
    options.technologyModuleId,
  );
  setNumericParam(
    searchParams,
    "technology_topic_id",
    options.technologyTopicId,
  );
  setNumericParam(
    searchParams,
    "technology_subtopic_id",
    options.technologySubtopicId,
  );
  setNumericParam(searchParams, "concept_id", options.conceptId);
  setNumericParam(searchParams, "question_type_id", options.questionTypeId);

  if (options.difficulty) {
    searchParams.set("difficulty", options.difficulty);
  }

  const search = options.search?.trim();
  if (search) {
    searchParams.set("search", search);
  }

  searchParams.set("suitability_tier", options.suitabilityTier ?? "recommended");

  const response = await adminFetch(
    `${API_URL}/admin/blueprint/generation-candidates?${searchParams.toString()}`,
  );

  if (!response.ok) {
    throw new Error(
      await readErrorMessage(
        response,
        "Failed to fetch blueprint generation candidates",
      ),
    );
  }

  return response.json();
}
