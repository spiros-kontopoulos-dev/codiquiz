# Question-service generation contracts
# Source: question-service/app/main.py (excerpt lines 54-180)
# Public portfolio excerpt; not standalone application code.

class GenerationRequest(BaseModel):
    # This contract mirrors one normalized quiz-api plan item.
    # The same shape is intentionally shared by mock, normal OpenAI, and later
    # Batch API execution so quiz-api does not care which provider created the draft.
    # language/category/topic are legacy compatibility fields; the active target
    # is Technology -> Domain -> Module -> Topic -> optional Subtopic -> optional Concept.
    language_id: int | None = None
    language_name: str | None = None
    category_id: int | None = None
    category_name: str | None = None
    topic_id: int | None = None
    topic_name: str | None = None
    technology_id: int | None = None
    technology_name: str | None = None
    technology_domain_id: int | None = None
    technology_domain_name: str | None = None
    technology_module_id: int | None = None
    technology_module_name: str | None = None
    technology_topic_id: int | None = None
    technology_topic_name: str | None = None
    technology_subtopic_id: int | None = None
    technology_subtopic_name: str | None = None
    primary_concept_id: int | None = None
    primary_concept_name: str | None = None
    question_type_id: int | None = None
    question_type_code: str | None = None
    question_type_name: str | None = None
    difficulty: str | None = None
    count: int = Field(..., ge=1, le=50)
    prompt_context: str | None = None
    model_profile: str | None = None
    generation_mode: Literal["normal", "reverse"] = "normal"
    taxonomy_slice: TaxonomySlice | None = None
    avoid_patterns: list[str] = Field(default_factory=list, max_length=15)

    # Development/test-only switch for mock generation. It lets quiz-api prove
    # classification failure and review paths without spending OpenAI tokens or
    # changing taxonomy rows. Real OpenAI generation ignores this field.
    mock_classification_case: Literal["missing", "invalid_ids", "low_confidence", "new_concept"] | None = None


class GeneratedAnswerOption(BaseModel):
    text: str = Field(..., min_length=1)
    is_correct: bool
    position: int = Field(..., ge=1, le=4)

    @field_validator("text")
    @classmethod
    def normalize_escaped_output_newlines(cls, value: str) -> str:
        # Output-prediction answer options sometimes come back from the model
        # as literal "\\n" text. Convert those escape sequences into real
        # newlines before quiz-api stores the draft.
        return normalize_escaped_text(value)


class GeneratedQuestionSuitabilitySuggestion(BaseModel):
    # BQE 1.30c: when reverse generation suggests a new concept, it can also
    # stage suitability-rule suggestions for that future concept. These are
    # review data only; quiz-api decides when/if they become real rules.
    suggested_question_type_id: int | None = None
    suggested_question_type_code: str | None = None
    suggested_question_type_name: str | None = None
    suitability_score: int | None = Field(default=None, ge=0, le=100)
    beginner_weight: float | None = Field(default=None, ge=0, le=3)
    intermediate_weight: float | None = Field(default=None, ge=0, le=3)
    advanced_weight: float | None = Field(default=None, ge=0, le=3)
    notes: str | None = None


class GeneratedQuestionClassification(BaseModel):
    # Reverse generation can classify each generated draft against the
    # selected local taxonomy slice. Normal generation returns null.
    suggested_subtopic_id: int | None = None
    suggested_subtopic_name: str | None = None
    suggested_concept_id: int | None = None
    suggested_concept_name: str | None = None
    suggested_question_type_id: int | None = None
    suggested_question_type_code: str | None = None
    suggested_question_type_name: str | None = None
    suggested_difficulty: str | None = None
    taxonomy_confidence: float | None = Field(default=None, ge=0, le=1)
    question_type_confidence: float | None = Field(default=None, ge=0, le=1)
    classification_reason: str | None = None
    suggested_new_concept_name: str | None = None
    suggested_new_concept_reason: str | None = None
    needs_taxonomy_review: bool = False
    suggested_suitability_rules: list[GeneratedQuestionSuitabilitySuggestion] = Field(default_factory=list)


class GeneratedQuestion(BaseModel):
    prompt: str = Field(..., min_length=1)
    code_snippet: str | None = None
    language_for_highlighting: str | None = None
    explanation: str | None = None
    difficulty: str | None = None
    time_limit_seconds: int | None = Field(default=None, ge=15, le=600)
    classification: GeneratedQuestionClassification | None = None
    answer_options: list[GeneratedAnswerOption] = Field(..., min_length=4, max_length=4)

    @model_validator(mode="after")
    def validate_multiple_choice_options(self):
        # The OpenAI schema enforces structure, but Pydantic remains the final
        # service-side gate before quiz-api stores anything in staging.
        correct_answer_count = sum(1 for option in self.answer_options if option.is_correct)
        if correct_answer_count != 1:
            raise ValueError("Each generated question must have exactly one correct answer.")

        positions = sorted(option.position for option in self.answer_options)
        if positions != [1, 2, 3, 4]:
            raise ValueError("Answer option positions must be exactly 1, 2, 3, and 4.")

        normalized_texts = [option.text.strip().casefold() for option in self.answer_options]
        if len(set(normalized_texts)) != len(normalized_texts):
            raise ValueError("Answer option text values must be unique within a question.")

        return self


class GenerationResponse(BaseModel):
    questions: list[GeneratedQuestion]
    provider: str | None = None
    model_profile: str | None = None
    model_used: str | None = None
    input_tokens: int | None = None
    output_tokens: int | None = None
    total_tokens: int | None = None
    prompt_version: str | None = None
