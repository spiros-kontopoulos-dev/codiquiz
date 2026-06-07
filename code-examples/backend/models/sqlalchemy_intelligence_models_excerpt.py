# Concept importance SQLAlchemy model
# Source: quiz-api/app/models.py (excerpt lines 375-430)
# Public portfolio excerpt; not standalone application code.

class ConceptImportance(Base):
    __tablename__ = "concept_importance"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    concept_id: Mapped[int] = mapped_column(ForeignKey("concepts.id"), nullable=False, unique=True, index=True)
    importance_tier: Mapped[str] = mapped_column(String(50), nullable=False, index=True)
    importance_score: Mapped[int] = mapped_column(Integer, nullable=False, index=True)
    reason: Mapped[str | None] = mapped_column(Text, nullable=True)
    source: Mapped[str] = mapped_column(String(50), nullable=False, default="admin", index=True)
    version: Mapped[str] = mapped_column(String(100), nullable=False, default="concept-importance-v1", index=True)
    created_at: Mapped[DateTime] = mapped_column(DateTime, nullable=False, server_default=func.now())
    updated_at: Mapped[DateTime] = mapped_column(DateTime, nullable=False, server_default=func.now(), onupdate=func.now())

    concept: Mapped["Concept"] = relationship("Concept", back_populates="importance")

    __table_args__ = (
        CheckConstraint(
            "importance_tier IN ('core', 'standard', 'niche', 'excluded')",
            name="ck_concept_importance_tier",
        ),
        CheckConstraint(
            "importance_score >= 0 AND importance_score <= 100",
            name="ck_concept_importance_score_range",
        ),
    )


class Language(Base):
    __tablename__ = "languages"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    code: Mapped[str] = mapped_column(String(50), nullable=False, unique=True, index=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)

    language_categories: Mapped[list["LanguageCategory"]] = relationship(
        "LanguageCategory",
        back_populates="language",
        cascade="all, delete-orphan",
    )


class Category(Base):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)

    # Compatibility field for the current question builder and old lookup route.
    # The new guided builder uses LanguageCategory below, but keeping this field
    # avoids breaking the existing working practice/question creation flow during
    # the taxonomy rebuild.
    language_id: Mapped[int] = mapped_column(ForeignKey("languages.id"), nullable=False)

    # Compatibility field for the old category/subcategory model.
    # New topic grouping is handled by Topic.parent_topic_id instead.
    parent_id: Mapped[int | None] = mapped_column(

# Question-type suitability and Blueprint rule models
# Source: quiz-api/app/models.py (excerpt lines 559-715)
# Public portfolio excerpt; not standalone application code.

class QuestionTypeSuitabilityRule(Base):
    __tablename__ = "question_type_suitability_rules"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)

    # scope_key stores the unique editor-facing target such as "module:14" or
    # "concept:205". Nullable foreign keys are still kept below for safe joins,
    # filtering, and future inheritance resolution.
    scope_key: Mapped[str] = mapped_column(String(100), nullable=False, index=True)
    scope_level: Mapped[str] = mapped_column(String(50), nullable=False, index=True)

    technology_module_id: Mapped[int | None] = mapped_column(
        ForeignKey("technology_modules.id"),
        nullable=True,
        index=True,
    )
    technology_topic_id: Mapped[int | None] = mapped_column(
        ForeignKey("technology_topics.id"),
        nullable=True,
        index=True,
    )
    technology_subtopic_id: Mapped[int | None] = mapped_column(
        ForeignKey("technology_subtopics.id"),
        nullable=True,
        index=True,
    )
    concept_id: Mapped[int | None] = mapped_column(
        ForeignKey("concepts.id"),
        nullable=True,
        index=True,
    )
    question_type_id: Mapped[int] = mapped_column(
        ForeignKey("question_types.id"),
        nullable=False,
        index=True,
    )

    suitability_score: Mapped[int] = mapped_column(Integer, nullable=False, default=80)
    beginner_weight: Mapped[Decimal] = mapped_column(Numeric(5, 2), nullable=False, default=Decimal("1.00"))
    intermediate_weight: Mapped[Decimal] = mapped_column(Numeric(5, 2), nullable=False, default=Decimal("1.00"))
    advanced_weight: Mapped[Decimal] = mapped_column(Numeric(5, 2), nullable=False, default=Decimal("1.00"))

    # Difficulty weights rank allowed difficulties. The boolean eligibility flags
    # are the hard gate used by Blueprint defaults and generation planning. This
    # prevents low-fit difficulties, such as beginner for advanced-only concepts,
    # from staying alive as weak-but-selectable automatic targets.
    beginner_allowed: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)
    intermediate_allowed: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)
    advanced_allowed: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)

    source: Mapped[str] = mapped_column(String(50), nullable=False, default="admin")
    profile: Mapped[str | None] = mapped_column(String(100), nullable=True)
    notes: Mapped[str | None] = mapped_column(Text, nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)
    created_at: Mapped[DateTime] = mapped_column(DateTime, nullable=False, server_default=func.now())
    updated_at: Mapped[DateTime] = mapped_column(DateTime, nullable=False, server_default=func.now(), onupdate=func.now())

    technology_module: Mapped["TechnologyModule | None"] = relationship(
        "TechnologyModule",
        back_populates="question_type_suitability_rules",
    )
    technology_topic: Mapped["TechnologyTopic | None"] = relationship(
        "TechnologyTopic",
        back_populates="question_type_suitability_rules",
    )
    technology_subtopic: Mapped["TechnologySubtopic | None"] = relationship(
        "TechnologySubtopic",
        back_populates="question_type_suitability_rules",
    )
    concept: Mapped["Concept | None"] = relationship(
        "Concept",
        back_populates="question_type_suitability_rules",
    )
    question_type: Mapped["QuestionType"] = relationship(
        "QuestionType",
        back_populates="suitability_rules",
    )

    __table_args__ = (
        UniqueConstraint(
            "scope_key",
            "question_type_id",
            name="uq_question_type_suitability_rules_scope_type",
        ),
    )


class BlueprintRule(Base):
    __tablename__ = "blueprint_rules"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)

    # Blueprint rules define the desired question-bank shape. The scope_key is
    # the stable resolver key, e.g. "global", "module:2", or "concept:205".
    # Nullable foreign keys are kept for safe joins and future scope filtering.
    scope_key: Mapped[str] = mapped_column(String(100), nullable=False, index=True)
    scope_level: Mapped[str] = mapped_column(String(50), nullable=False, index=True)

    taxonomy_field_id: Mapped[int | None] = mapped_column(
        ForeignKey("taxonomy_fields.id"),
        nullable=True,
        index=True,
    )
    technology_id: Mapped[int | None] = mapped_column(
        ForeignKey("technologies.id"),
        nullable=True,
        index=True,
    )
    technology_domain_id: Mapped[int | None] = mapped_column(
        ForeignKey("technology_domains.id"),
        nullable=True,
        index=True,
    )
    technology_module_id: Mapped[int | None] = mapped_column(
        ForeignKey("technology_modules.id"),
        nullable=True,
        index=True,
    )
    technology_topic_id: Mapped[int | None] = mapped_column(
        ForeignKey("technology_topics.id"),
        nullable=True,
        index=True,
    )
    technology_subtopic_id: Mapped[int | None] = mapped_column(
        ForeignKey("technology_subtopics.id"),
        nullable=True,
        index=True,
    )
    concept_id: Mapped[int | None] = mapped_column(
        ForeignKey("concepts.id"),
        nullable=True,
        index=True,
    )

    # NULL question_type_id means "all allowed question types". NULL difficulty
    # means "all applicable difficulties". The coverage engine expands these
    # broad rules into concrete concept/type/difficulty cells later.
    question_type_id: Mapped[int | None] = mapped_column(
        ForeignKey("question_types.id"),
        nullable=True,
        index=True,
    )
    difficulty: Mapped[str | None] = mapped_column(String(50), nullable=True, index=True)

    target_count: Mapped[int] = mapped_column(Integer, nullable=False, default=2)
    priority: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    source: Mapped[str] = mapped_column(String(50), nullable=False, default="admin")
    notes: Mapped[str | None] = mapped_column(Text, nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True, index=True)
    created_at: Mapped[DateTime] = mapped_column(DateTime, nullable=False, server_default=func.now())
    updated_at: Mapped[DateTime] = mapped_column(DateTime, nullable=False, server_default=func.now(), onupdate=func.now())

    taxonomy_field: Mapped["TaxonomyField | None"] = relationship("TaxonomyField")
    technology: Mapped["Technology | None"] = relationship("Technology")
    technology_domain: Mapped["TechnologyDomain | None"] = relationship("TechnologyDomain")
    technology_module: Mapped["TechnologyModule | None"] = relationship("TechnologyModule")
    technology_topic: Mapped["TechnologyTopic | None"] = relationship("TechnologyTopic")

# AI execution job and generated draft models
# Source: quiz-api/app/models.py (excerpt lines 1545-1668)
# Public portfolio excerpt; not standalone application code.

class AIGenerationExecutionJob(Base):
    __tablename__ = "ai_generation_execution_jobs"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    batch_id: Mapped[int] = mapped_column(
        ForeignKey("ai_generation_batches.id"),
        nullable=False,
        index=True,
    )
    plan_item_id: Mapped[int] = mapped_column(
        ForeignKey("ai_generation_plan_items.id"),
        nullable=False,
        index=True,
    )

    # One execution job represents one provider/API call for one normalized
    # plan item. Large normal-API plan items are split into small chunks, while
    # retries and future Batch API submissions can create additional attempts
    # without changing the original requested plan.
    attempt_number: Mapped[int] = mapped_column(Integer, nullable=False, default=1)
    chunk_index: Mapped[int] = mapped_column(Integer, nullable=False, default=1)
    chunk_count: Mapped[int] = mapped_column(Integer, nullable=False, default=1)
    retry_of_job_id: Mapped[int | None] = mapped_column(
        ForeignKey("ai_generation_execution_jobs.id"),
        nullable=True,
        index=True,
    )
    retry_reason: Mapped[str | None] = mapped_column(Text, nullable=True)
    status: Mapped[str] = mapped_column(String(50), nullable=False, default="pending")
    provider: Mapped[str | None] = mapped_column(String(50), nullable=True)
    execution_mode: Mapped[str] = mapped_column(String(50), nullable=False, default="normal_api")
    model_profile: Mapped[str | None] = mapped_column(String(100), nullable=True)
    model_used: Mapped[str | None] = mapped_column(String(150), nullable=True)
    provider_batch_id: Mapped[str | None] = mapped_column(String(150), nullable=True, index=True)
    provider_request_custom_id: Mapped[str | None] = mapped_column(String(200), nullable=True, index=True)
    provider_response_json: Mapped[str | None] = mapped_column(Text, nullable=True)
    provider_error_json: Mapped[str | None] = mapped_column(Text, nullable=True)
    provider_result_collected_at: Mapped[DateTime | None] = mapped_column(DateTime, nullable=True)

    requested_count: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    generated_count: Mapped[int] = mapped_column(Integer, nullable=False, default=0)

    actual_input_tokens: Mapped[int | None] = mapped_column(Integer, nullable=True)
    actual_output_tokens: Mapped[int | None] = mapped_column(Integer, nullable=True)
    actual_total_tokens: Mapped[int | None] = mapped_column(Integer, nullable=True)
    actual_cost_usd: Mapped[Decimal | None] = mapped_column(Numeric(12, 6), nullable=True)
    pricing_snapshot_json: Mapped[str | None] = mapped_column(Text, nullable=True)
    error_category: Mapped[str | None] = mapped_column(String(100), nullable=True)
    error_message: Mapped[str | None] = mapped_column(Text, nullable=True)

    created_at: Mapped[DateTime] = mapped_column(
        DateTime,
        nullable=False,
        server_default=func.now(),
    )
    started_at: Mapped[DateTime | None] = mapped_column(DateTime, nullable=True)
    completed_at: Mapped[DateTime | None] = mapped_column(DateTime, nullable=True)

    batch: Mapped["AIGenerationBatch"] = relationship(
        "AIGenerationBatch",
        back_populates="execution_jobs",
    )
    plan_item: Mapped["AIGenerationPlanItem"] = relationship(
        "AIGenerationPlanItem",
        back_populates="execution_jobs",
    )
    retry_of_job: Mapped["AIGenerationExecutionJob | None"] = relationship(
        "AIGenerationExecutionJob",
        remote_side="AIGenerationExecutionJob.id",
    )

    __table_args__ = (
        UniqueConstraint(
            "plan_item_id",
            "chunk_index",
            "attempt_number",
            name="uq_ai_generation_execution_job_plan_item_chunk_attempt",
        ),
    )


class AIGeneratedQuestion(Base):
    __tablename__ = "ai_generated_questions"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    batch_id: Mapped[int] = mapped_column(
        ForeignKey("ai_generation_batches.id"),
        nullable=False,
        index=True,
    )
    plan_item_id: Mapped[int] = mapped_column(
        ForeignKey("ai_generation_plan_items.id"),
        nullable=False,
        index=True,
    )

    # Draft question content produced by AI. It is intentionally separate from
    # the public question bank until an admin reviews and approves it.
    prompt: Mapped[str] = mapped_column(Text, nullable=False)
    code_snippet: Mapped[str | None] = mapped_column(Text, nullable=True)
    language_for_highlighting: Mapped[str | None] = mapped_column(String(50), nullable=True)
    explanation: Mapped[str | None] = mapped_column(Text, nullable=True)

    difficulty: Mapped[str | None] = mapped_column(String(50), nullable=True)
    language_id: Mapped[int | None] = mapped_column(ForeignKey("languages.id"), nullable=True)
    category_id: Mapped[int | None] = mapped_column(ForeignKey("categories.id"), nullable=True)
    topic_id: Mapped[int | None] = mapped_column(ForeignKey("topics.id"), nullable=True)
    question_type_id: Mapped[int | None] = mapped_column(
        ForeignKey("question_types.id"),
        nullable=True,
    )

    technology_id: Mapped[int | None] = mapped_column(ForeignKey("technologies.id"), nullable=True, index=True)
    technology_domain_id: Mapped[int | None] = mapped_column(ForeignKey("technology_domains.id"), nullable=True, index=True)
    technology_module_id: Mapped[int | None] = mapped_column(ForeignKey("technology_modules.id"), nullable=True, index=True)
    technology_topic_id: Mapped[int | None] = mapped_column(ForeignKey("technology_topics.id"), nullable=True, index=True)
    technology_subtopic_id: Mapped[int | None] = mapped_column(ForeignKey("technology_subtopics.id"), nullable=True, index=True)
    primary_concept_id: Mapped[int | None] = mapped_column(ForeignKey("concepts.id"), nullable=True, index=True)

    # Reverse generation first produces a broad draft, then asks AI/Codiquiz to
    # classify the draft into the precise taxonomy/question-type metadata that
    # should be reviewed before approval. These suggested fields are separate
    # from the actual approved-target fields above so admins can compare, adjust,
    # and normalize AI suggestions before they become canonical question bank data.
