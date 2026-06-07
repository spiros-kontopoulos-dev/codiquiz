// Selected sanitized excerpt from Codiquiz AI generation TypeScript API client.
// Shows typed frontend contracts for plan preview, batch creation/run, settings, and execution mode.
// This is partial and is not intended to compile standalone.

import { adminFetch } from "./auth";

const API_BASE_URL = import.meta.env.VITE_API_URL ?? "http://localhost:8000";

export type AiGenerationAllocationStrategy = "manual" | "equal" | "random" | "weighted";
export type AiGenerationGenerationMode = "normal" | "reverse";
export type AiGenerationProvider = "mock" | "openai";
export type AiGenerationExecutionMode = "normal_api" | "batch_api";
export type AiGenerationModelProfile =
  | "mock"
  | "budget_draft"
  | "balanced_draft"
  | "premium_advanced"
  | "validation_only";
export type AiGenerationReviewDecision = "approve" | "reject";
export type AiClassificationStatus = "not_applicable" | "passed" | "review" | "failed" | "mismatch";
export type AiClassificationStatusReason =
  | "passed"
  | "missing"
  | "invalid_ids"
  | "low_confidence"
  | "new_concept"
  | "needs_review"
  | "target_mismatch"
  | "review_done";
export type AiGenerationBlueprintAlignmentStatus =
  | "gap_fill"
  | "expansion"
  | "over_expansion_cap"
  | "outside_blueprint_target"
  | "needs_mapping_review";
export type AiGenerationBatchSortField =
  | "id"
  | "status"
  | "requested_count"
  | "planned_count"
  | "generated_count"
  | "approved_count"
  | "rejected_count"
  | "actual_cost_usd"
  | "repetition_rate"
  | "created_at";
export type AiGenerationSortDirection = "asc" | "desc";
export type AiGenerationBatchArchiveStatus = "active" | "archived" | "all";
export type AiGenerationBatchRepetitionBucket = "clean" | "low" | "medium" | "high";
export type AiGenerationBatchReviewStatus =
  | "no_drafts"
  | "pending_review"
  | "partially_approved"
  | "has_approved"
  | "fully_reviewed"
  | "has_rejected";
export type AiGenerationBatchExecutionModeFilter = "normal_api" | "batch_api";

export type AiGenerationPlanGroup = {
  requested_count?: number | null;
  weight?: number | null;
  generation_mode?: AiGenerationGenerationMode;
  language_id?: number | null;
  category_id?: number | null;
  topic_ids?: number[];
  technology_id?: number | null;
  technology_domain_id?: number | null;
  technology_module_ids?: number[];
  technology_topic_ids?: number[];
  technology_subtopic_ids?: number[];
  primary_concept_ids?: number[];
  question_type_ids?: number[];
  difficulties?: string[];
  prompt_context?: string | null;
};

export type AiGenerationPlanItemInput = {
  requested_count: number;
  generation_mode?: AiGenerationGenerationMode;
  language_id?: number | null;
  category_id?: number | null;
  topic_id?: number | null;
  technology_id?: number | null;
  technology_domain_id?: number | null;
  technology_module_id?: number | null;
  technology_topic_id?: number | null;
  technology_subtopic_id?: number | null;
  primary_concept_id?: number | null;
  question_type_id?: number | null;
  difficulty?: string | null;
  prompt_context?: string | null;
};

export type AiGenerationCreateRequest = {
  requested_count: number;
  allocation_strategy: AiGenerationAllocationStrategy;
  generation_mode?: AiGenerationGenerationMode;
  language_id?: number | null;
  category_ids?: number[];
  topic_ids?: number[];
  technology_id?: number | null;
  technology_domain_ids?: number[];
  technology_module_ids?: number[];
  technology_topic_ids?: number[];
  technology_subtopic_ids?: number[];
  primary_concept_ids?: number[];
  question_type_ids?: number[];
  difficulties?: string[];
  groups?: AiGenerationPlanGroup[];
  plan_items?: AiGenerationPlanItemInput[];
  random_seed?: number | null;
  source_model?: string | null;
  prompt_version?: string | null;
  prompt_instructions?: string | null;
};

export type AiGenerationBlueprintPriorityBucket = "none" | "low" | "medium" | "high" | "top";
export type AiGenerationBlueprintSuitabilityTier =
  | "strong"
  | "secondary"
  | "weak"
  | "unrated"
  | "excluded";
export type AiGenerationBlueprintMetadataSource =
  | "blueprint_candidate"
  | "blueprint_lookup";

export type AiGenerationPlanItemPreview = {
  position: number;
  requested_count: number;
  generation_mode: AiGenerationGenerationMode;
  language_id: number | null;
  language_name: string | null;
  category_id: number | null;
  category_name: string | null;
  topic_id: number | null;
  topic_name: string | null;
  technology_id: number | null;
  technology_name: string | null;
  technology_domain_id: number | null;
  technology_domain_name: string | null;
  technology_module_id: number | null;
  technology_module_name: string | null;
  technology_topic_id: number | null;
  technology_topic_name: string | null;
  technology_subtopic_id: number | null;
  technology_subtopic_name: string | null;
  primary_concept_id: number | null;
  primary_concept_name: string | null;
  question_type_id: number | null;
  question_type_name: string | null;
  difficulty: string | null;
  prompt_context: string | null;
  blueprint_generation_priority_score?: number | null;
  blueprint_generation_priority_bucket?: AiGenerationBlueprintPriorityBucket | null;
  blueprint_generation_priority_reasons?: string[];
  blueprint_suitability_score?: number | null;
  blueprint_suitability_tier?: AiGenerationBlueprintSuitabilityTier | null;
  blueprint_target_count?: number | null;
  blueprint_hard_gap_count?: number | null;
  blueprint_effective_gap_count?: number | null;
  blueprint_pending_review_count?: number | null;
  blueprint_rule_id?: number | null;
  blueprint_rule_scope_key?: string | null;
  blueprint_metadata_source?: AiGenerationBlueprintMetadataSource | null;
};

export type AiGenerationPlanPreview = {
  requested_count: number;
  planned_count: number;
  generation_mode: AiGenerationGenerationMode;
  plan_item_count: number;
  allocation_strategy: AiGenerationAllocationStrategy;
  plan_items: AiGenerationPlanItemPreview[];
