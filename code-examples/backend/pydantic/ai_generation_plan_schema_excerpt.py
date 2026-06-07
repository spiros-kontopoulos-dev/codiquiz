# Pydantic AI generation plan schemas
# Source: quiz-api/app/schemas_ai_generation.py (excerpt lines 29-125)
# Public portfolio excerpt; not standalone application code.

class AIGenerationPlanItemInput(BaseModel):
    # Explicit/manual generation target. The active target is the new taxonomy;
    # legacy language/category/topic fields are accepted only for compatibility.
    requested_count: int = Field(..., ge=1)
    generation_mode: AIGenerationMode = Field(default="normal")
    language_id: int | None = None
    category_id: int | None = None
    topic_id: int | None = None
    technology_id: int | None = None
    technology_domain_id: int | None = None
    technology_module_id: int | None = None
    technology_topic_id: int | None = None
    technology_subtopic_id: int | None = None
    primary_concept_id: int | None = None
    question_type_id: int | None = None
    difficulty: str | None = None
    prompt_context: str | None = None


class AIGenerationAllocationGroupInput(BaseModel):
    # A group represents one allocation pool. For the new taxonomy this usually
    # means one Technology/Domain plus selected module/topic/concept/type/difficulty combinations.
    requested_count: int | None = Field(default=None, ge=1)
    weight: int | None = Field(default=None, ge=1)
    generation_mode: AIGenerationMode = Field(default="normal")
    language_id: int | None = None
    category_id: int | None = None
    topic_ids: list[int] = Field(default_factory=list)
    technology_id: int | None = None
    technology_domain_id: int | None = None
    technology_module_ids: list[int] = Field(default_factory=list)
    technology_topic_ids: list[int] = Field(default_factory=list)
    technology_subtopic_ids: list[int] = Field(default_factory=list)
    primary_concept_ids: list[int] = Field(default_factory=list)
    question_type_ids: list[int] = Field(default_factory=list)
    difficulties: list[str] = Field(default_factory=list)
    prompt_context: str | None = None


class AIGenerationPlanCreate(BaseModel):
    requested_count: int = Field(..., ge=1)
    allocation_strategy: str = Field(default="manual")
    generation_mode: AIGenerationMode = Field(default="normal")

    # Optional seed used only for random allocation. Supplying it makes preview
    # and create requests reproducible, which is useful once the admin UI shows
    # a random plan before saving it.
    random_seed: int | None = None

    # Legacy target fields accepted temporarily for old clients/saved workflows.
    language_id: int | None = None
    category_ids: list[int] = Field(default_factory=list)
    topic_ids: list[int] = Field(default_factory=list)

    # New content taxonomy target fields.
    technology_id: int | None = None
    technology_domain_ids: list[int] = Field(default_factory=list)
    technology_module_ids: list[int] = Field(default_factory=list)
    technology_topic_ids: list[int] = Field(default_factory=list)
    technology_subtopic_ids: list[int] = Field(default_factory=list)
    primary_concept_ids: list[int] = Field(default_factory=list)

    # Cross-cutting assessment settings.
    question_type_ids: list[int] = Field(default_factory=list)
    difficulties: list[str] = Field(default_factory=list)

    # Advanced allocation fields.
    groups: list[AIGenerationAllocationGroupInput] = Field(default_factory=list)
    plan_items: list[AIGenerationPlanItemInput] = Field(default_factory=list)

    source_model: str | None = None
    prompt_version: str | None = None
    prompt_instructions: str | None = None

    @model_validator(mode="after")
    def validate_strategy_payload(self):
        allowed_strategies = {"manual", "equal", "random", "weighted"}
        if self.allocation_strategy not in allowed_strategies:
            raise ValueError("allocation_strategy must be one of: manual, equal, random, weighted")

        plan_items_use_new_taxonomy = any(
            item.technology_id is not None
            or item.technology_domain_id is not None
            or item.technology_module_id is not None
            or item.technology_topic_id is not None
            or item.technology_subtopic_id is not None
            or item.primary_concept_id is not None
            for item in self.plan_items
        )
        uses_new_taxonomy = self.technology_id is not None or plan_items_use_new_taxonomy or any(
            [
                self.technology_domain_ids,
                self.technology_module_ids,
                self.technology_topic_ids,
                self.technology_subtopic_ids,
                self.primary_concept_ids,
            ]
