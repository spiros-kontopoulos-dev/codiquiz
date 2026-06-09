# Commit History

Repository: ai-quiz-platform
Branch: main
Generated: 2026-06-10 00:52:37 +03:00
Total commits: 417
Latest commit: `660f6d2`

## 2026-06-09 - `660f6d2`

**Author:** Spiros Kontopoulos

**Full commit:** `660f6d211ceb9f2fb12faf29832bb66e5fd63d4f`

Update private Codiquiz documentation for practice and AI cost systems

- Document Quick Practice, Custom Practice, Try Concept, and Concept Finder
- Add quiz technology filtering and promoted/coming-soon quiz documentation
- Document AI model profile visibility, editable mappings, pricing catalog, and tiktoken estimates
- Refresh AI generation workflow, serving, roadmap, and engineering highlights

## 2026-06-09 - `3e30da1`

**Author:** Spiros Kontopoulos

**Full commit:** `3e30da1d91ef8b293540cc2abcb68aa0d44e9f4b`

Add tiktoken AI generation cost estimates

- Add tiktoken-backed token estimation for pre-generation cost previews
- Keep actual post-generation cost tracking based on provider usage
- Include tokenizer method and fallback metadata in cost estimate responses
- Use configured model pricing for standard and Batch API estimates

## 2026-06-09 - `3b81ce0`

**Author:** Spiros Kontopoulos

**Full commit:** `3b81ce0c58084b65974900c9b475958f9379f384`

Add editable AI model profile mappings

- Add DB-backed model profile configuration for AI generation
- Add OpenAI model pricing catalog with input, output, and Batch API costs
- Show relative model cost comparisons in admin settings
- Allow admins to change profile-to-model mappings from the settings page
- Resolve generation profiles to configured provider models before provider calls

## 2026-06-09 - `e93a5a0`

**Author:** Spiros Kontopoulos

**Full commit:** `e93a5a0871c2dfc71352493ac5723b21c685ccab`

Add AI generation cost and quality dashboard

- Replace the cost-quality placeholder with a real admin dashboard
- Add backend summary metrics for generated, approved, rejected, pending, and duplicate-warning drafts
- Show estimated cost, approval rates, and cost per approved question
- Add profile/provider/model breakdown and latest generation outcomes

## 2026-06-09 - `b8ec812`

**Author:** Spiros Kontopoulos

**Full commit:** `b8ec812deea8c3a1aeb30c462a3dcaf2f6ab20a5`

Add AI model profile visibility to admin settings

- Expose admin-readable AI model profile metadata
- Show provider, model, purpose, config source, and compatibility in settings
- Clarify stable profile keys versus raw provider model resolution
- Preserve current generation behavior while improving admin visibility

## 2026-06-09 - `3571c32`

**Author:** Spiros Kontopoulos

**Full commit:** `3571c32cef4404de31e81370fcd8ff92259bb705`

Update public and admin smoke tests

- Cover updated public practice routes and Try Concept flow
- Align Quick Practice smoke tests with domain-based setup
- Relax admin smoke assertions for renamed sections
- Allow session-start smoke to skip when no approved quick-practice target exists

## 2026-06-09 - `29471f1`

**Author:** Spiros Kontopoulos

**Full commit:** `29471f1a59ca442b609d08791d1ab74a7ef12545`

Add public concept help hints

- Explain concepts in the Try Concept finder
- Add concept guidance to Custom Practice concept focus
- Show concept explanation above technology-page concept rows
- Keep the explanation lightweight and reusable across public flows

## 2026-06-08 - `c5988e9`

**Author:** Spiros Kontopoulos

**Full commit:** `c5988e9d50098d6d165063e1cf6996a3568a0582`

Polish quiz technology filters and public practice links

- Load public quiz technology filters dynamically
- Add pagination-ready quiz grid polish
- Show promoted quiz New badges on the homepage
- Link homepage concept preview to Try Concept
- Update locked practice step icons with warm accent styling

## 2026-06-08 - `602dcbc`

**Author:** Spiros Kontopoulos

**Full commit:** `602dcbc28a8bf12269372611aece927cdf825ca5`

Attach quizzes to technologies

- Add technology metadata and relationship for quizzes
- Backfill existing quizzes to Python through migration
- Add quiz API filtering by technology slug
- Return quiz technology metadata to the frontend
- Use real quiz technology data in the public quiz list

## 2026-06-08 - `4c6571e`

**Author:** Spiros Kontopoulos

**Full commit:** `4c6571ea724a4753011bb0dd2881eb5e5fabdc95`

Attach quizzes to technologies

- Add technology metadata and relationship for quizzes
- Backfill existing quizzes to Python through migration
- Add quiz API filtering by technology slug
- Return quiz technology metadata to the frontend
- Use real quiz technology data in the public quiz list

## 2026-06-08 - `d73fb30`

**Author:** Spiros Kontopoulos

**Full commit:** `d73fb30f0f74da5b379e90e62c6b1e2498b5167e`

Polish practice results and quiz list UI

- Show completed practice sessions with a relevant results header
- Remove generic setup heading from completed practice results
- Add a lightweight technology selector to the public quiz list
- Show Python technology styling on quiz cards as a temporary frontend-safe fallback

## 2026-06-08 - `99fc5e7`

**Author:** Spiros Kontopoulos

**Full commit:** `99fc5e73c048753385a5f410a4abaa6ade15ae1d`

Guard active practice sessions during navigation

- Reload public nav links when clicking the current route again
- Show the Codiquiz stop-session confirmation before internal navigation
- Continue navigation only after the user confirms abandoning the session
- Add browser-level warning for refresh, close, or back during active sessions

## 2026-06-08 - `d4e5180`

**Author:** Spiros Kontopoulos

**Full commit:** `d4e518078c91d7d14fb71012ed1451fd0248fe5c`

Support deeper practice availability filters

- Filter practice availability by selected subtopics and concepts
- Add backend support for subtopic and multi-concept practice filters
- Allow Custom Practice module apply to mean any selected-domain module
- Add per-domain module select and clear controls

## 2026-06-08 - `d11d280`

**Author:** Spiros Kontopoulos

**Full commit:** `d11d280baaaf8ad2c2bdedf15422bb0674140b58`

Align practice results with quiz review UI

- Reuse question-card style for practice result review
- Show correct, wrong, and unanswered status pills
- Label selected and correct answer rows inside the answer list
- Remove old separate answer-summary result layout

## 2026-06-08 - `f3a3a17`

**Author:** Spiros Kontopoulos

**Full commit:** `f3a3a178cfeda9d330a08fc67b838b94efe80559`

Fix public practice path links and quick domain selection

- Keep recommended practice path links scoped to their own taxonomy targets
- Allow Quick Practice to combine up to three domains
- Update Quick Practice copy for multi-domain selection
- Improve active session scroll positioning

## 2026-06-08 - `3f49743`

**Author:** Spiros Kontopoulos

**Full commit:** `3f49743358befda49bbe23cf9e6664453f4c2b55`

Polish public practice question UI

- Add answer labels and compact active question layout
- Add custom stop-session confirmation modal
- Hide generic practice setup heading during active sessions
- Reset scroll on route changes and focus active questions during sessions

## 2026-06-08 - `3eb489e`

**Author:** Spiros Kontopoulos

**Full commit:** `3eb489e3b42b09a160a61df279775874c9552a78`

Add one-question Try Concept flow

- Add public endpoint for fetching one concept question by question type
- Replace question-style cards with an inline try-question view
- Add local answer feedback with explanation display
- Add try-another-question and choose-another-style actions

## 2026-06-08 - `95e73f8`

**Author:** Spiros Kontopoulos

**Full commit:** `95e73f8dffd95a4d718319a6ccfb4e1d51f47fbb`

Add Try Concept question style options

- Add public concept question-type options endpoint
- Show strong and secondary question styles for selected concepts
- Display suitability score, approved count, and allowed difficulties
- Keep one-question Try Concept flow for the next patch

## 2026-06-08 - `f53a029`

**Author:** Spiros Kontopoulos

**Full commit:** `f53a029d540976893cbc9faab6c0713bdca92868`

Add public Try Concept finder

- Add searchable public concept finder for Try Concept
- Add numbered pagination and 10-result pages
- Prioritize concepts with approved questions
- Add practice landing cards for Try Concept and future question-type mode

## 2026-06-08 - `61c8c9f`

**Author:** Spiros Kontopoulos

**Full commit:** `61c8c9ffc9afa1283b7d3328d98034e7a4d15f05`

Add Try Concept practice entry route

- Add public Try Concept route and practise redirect alias
- Rename concept-level taxonomy actions to Try Concept
- Pass selected concept and taxonomy path into the Try Concept route
- Add placeholder state for the future concept finder flow

## 2026-06-08 - `9f3a83b`

**Author:** Spiros Kontopoulos

**Full commit:** `9f3a83b63f311110451422c83e8b172f21c8f554`

Polish custom practice taxonomy selection

- Open prefilled practice sessions at the next relevant taxonomy step
- Show full taxonomy paths for topic, subtopic, and concept groups
- Add per-group select and clear controls for concepts
- Keep concept-specific practice mode deferred for later

## 2026-06-08 - `c971420`

**Author:** Spiros Kontopoulos

**Full commit:** `c9714205bc3e70943f7ce6011f81495ba4c53741`

Add public practice mode routes and taxonomy prefill

- Add practice landing page with quick and custom mode cards
- Add quick and custom practice routes with practise redirects
- Prefill custom practice from taxonomy path query parameters
- Link taxonomy quick/custom actions to the correct practice modes

## 2026-06-08 - `b70e66a`

**Author:** Spiros Kontopoulos

**Full commit:** `b70e66a9ed8f2eee373f898d9646b2a6625a9380`

Polish public homepage interactions

- Remove experimental stats flip animation
- Keep static technology stats badge and live stat values
- Preserve hero-card pause, taxonomy path preview, and practice links
- Keep ranking mode disabled as coming soon

## 2026-06-08 - `27c5eb8`

**Author:** Spiros Kontopoulos

**Full commit:** `27c5eb8147909cc86af398b8580589d07b942871`

Polish public taxonomy sidebar navigation

- Move the taxonomy sidebar toward the earlier compact tree style
- Replace noisy semantic sidebar icons with simple hierarchy markers
- Keep technology branding while simplifying domain/module/topic rows
- Preserve active row, indentation, and expand-collapse behavior

## 2026-06-08 - `2ca3a7d`

**Author:** Spiros Kontopoulos

**Full commit:** `2ca3a7d3121db74a3c149f527321a44fe7100d43`

Polish public taxonomy and practice UI

- Show approved question count on the current taxonomy scope
- Keep Quick Practice and Start Quiz actions while clarifying available content
- Fix quick-practice side-card overlap on smaller screens
- Remove fake homepage stat and quiz fallbacks
- Lighten Python taxonomy tree icons and simplify back button wording

## 2026-06-08 - `83f995a`

**Author:** Spiros Kontopoulos

**Full commit:** `83f995a48f58456dc823a32496dd30c79eaa337e`

Add reverse scope coverage estimate

- Show recommended open Blueprint gaps for reverse-mode scopes
- Reuse Blueprint default-target summaries for module/topic/subtopic/concept estimates
- Add suggested reverse request-size buttons based on open gap and active concepts
- Avoid showing raw all-possible cell counts in broad reverse mode
- Fix Create Generation side-rail overlap on smaller screens

## 2026-06-07 - `8fe9bc8`

**Author:** Spiros Kontopoulos

**Full commit:** `8fe9bc8d521408ee09e9fc84b94317aae9f3e75d`

Normalize AI difficulty labels in generation

- Map common AI difficulty aliases to Codiquiz canonical labels
- Normalize reverse-mode classification difficulty before staging
- Normalize generated question difficulty before storing drafts
- Add prompt rules requiring beginner/intermediate/advanced values
- Keep unknown difficulty labels visible as validation review messages

## 2026-06-07 - `f804a5a`

**Author:** Spiros Kontopoulos

**Full commit:** `f804a5af33fccaa6f10bf1a475250b1a2d4af1a6`

Polish dashboard and activity tracking views

- Remove create-question shortcut from the admin dashboard
- Make taxonomy management the primary dashboard action
- Add clickable session/event view blocks to admin activity
- Add clickable session/page-view blocks to public tracking
- Restore admin session API/types required by the polished activity UI

## 2026-06-07 - `f40fb87`

**Author:** Spiros Kontopoulos

**Full commit:** `f40fb870a196c0bf4b4f55747617696ccdac105f`

Add geolocation variables for docker prod and env file

## 2026-06-07 - `a44fa47`

**Author:** Spiros Kontopoulos

**Full commit:** `a44fa47d3b5cb731f6f7fee23e56c58315349ef6`

Add GeoIP tracking visibility and owner exclusions

- Add MaxMind GeoIP2 City dependency and shared public/admin location lookup
- Add owner-managed public tracking exclusion table and API
- Add Owner tools panel for excluding/re-enabling the current network
- Skip public visitor tracking for excluded network hashes
- Hide owner admin activity from default visibility dashboards

## 2026-06-07 - `5aa89d6`

**Author:** Spiros Kontopoulos

**Full commit:** `5aa89d6db7299b6ca8678e19d4f62be529537cde`

Add GeoIP foundation for demo access visibility

- Add privacy-safe optional GeoIP location resolver
- Resolve location metadata for admin and demo auth sessions
- Expose owner-only GeoIP configuration status endpoint
- Include GeoIP config state in demo visibility summary
- Document deployment requirements for local GeoIP database lookup

## 2026-06-07 - `37adf76`

**Author:** Spiros Kontopoulos

**Full commit:** `37adf76ab6307aa71ae85cce7f8d4aa6343e1762`

Add admin visibility for temporary demo access

- Add owner-facing visibility cards in Users / Access
- Show temporary demo accounts separately from manual demo viewers
- Add demo request history and admin/demo session visibility
- Display safe network and prepared location metadata without raw IPs
- Add owner revoke action for temporary demo accounts

## 2026-06-07 - `d4523c5`

**Author:** Spiros Kontopoulos

**Full commit:** `d4523c5abddd8db5d3a0dfa0376551240db0aeee`

Add backend visibility for temporary demo access

- Add owner-only APIs for temporary demo accounts, requests, and sessions
- Store safe network and placeholder location metadata for demo/admin access
- Separate manual demo viewers from self-service temporary demo accounts
- Add owner revoke endpoint for temporary demo accounts
- Prepare fields for later GeoIP country and city resolution

## 2026-06-07 - `6d55a67`

**Author:** Spiros Kontopoulos

**Full commit:** `6d55a67ce3d37697d207a0c976c974b4d13176ce`

Finalize temporary admin demo access hardening

- Remove preview-specific wording from reusable demo/error UI
- Add noindex handling for admin API and admin SPA pages
- Document demo access limits, expiry, permissions, and deployment requirements
- Add smoke-test checklist and optional PowerShell demo access test helper
- Keep geolocation visibility documented as a separate follow-up feature

## 2026-06-07 - `c9416fd`

**Author:** Spiros Kontopoulos

**Full commit:** `c9416fd058ba4aa4c32e3fd1ef869a17d316ebbd`

Refine demo access limits and wording

- Lower default active demo account cap to 10
- Keep practical per-network limits visible on the demo access page
- Avoid exposing technical global-cap wording to reviewers
- Use a friendlier temporary-capacity message

## 2026-06-07 - `62f6e78`

**Author:** Spiros Kontopoulos

**Full commit:** `62f6e78b15fbe144ed9ed9a2137321dbd453cb14`

Add temporary admin demo access page

- Add public-but-unlisted admin demo access route
- Add optional identity form and rate-limit explanation
- Show generated username/password credentials once on screen
- Add copy/login actions for demo reviewers
- Replace default route errors with friendly admin error pages

## 2026-06-07 - `145f1e0`

**Author:** Spiros Kontopoulos

**Full commit:** `145f1e0f243498fa9ab27ae6377925e9fefae9fd`

Enforce temporary admin demo access expiry

- Reject expired demo accounts during login and authenticated requests
- Start demo access window on first successful login
- Cap demo session and cookie lifetime to demo expiry
- Add two-hour cleanup task for expired demo accounts
- Return username-only visible demo credentials

## 2026-06-07 - `efb45c4`

**Author:** Spiros Kontopoulos

**Full commit:** `efb45c4a68943fcb2ea6fcba48ed27dbb912c445`

Add temporary admin demo access generation

- Add demo account lifecycle fields and access request audit table
- Add public demo access credential generation endpoint
- Enforce initial rate limits and global active demo cap
- Store request IPs as peppered hashes instead of raw addresses

## 2026-06-07 - `f0c0fb0`

**Author:** Spiros Kontopoulos

**Full commit:** `f0c0fb03295f89dfe5927c0c026b9151fdb7faf5`

Document backend intelligence layer

- Add Backend Intelligence Layer documentation
- Update README with concept importance, suitability, and Blueprint defaults
- Refresh Blueprint and suitability docs with current implemented behavior
- Update roadmap and portfolio highlights for recent intelligence work

## 2026-06-07 - `81ca063`

**Author:** Spiros Kontopoulos

**Full commit:** `81ca0634ecc00420a3a52cb03147fa40497e8540`

Add preview showcase readiness docs

- Add DEPLOY 1.5 preview showcase checklist
- Document recruiter/demo walkthrough flow
- Document demo account safety boundaries
- Add safe public wording for live preview status

## 2026-06-07 - `f7324d2`

**Author:** Spiros Kontopoulos

**Full commit:** `f7324d2d0988aa4e9a3970f7c7e29ad3b4d63e0e`

Harden preview backup database detection

- Remove silent fallback to local dev database defaults
- Detect Postgres database and role from the running container
- Print resolved database/user sources during backup runs
- Add clear failure guidance when database detection cannot resolve values

## 2026-06-07 - `e97d44d`

**Author:** Spiros Kontopoulos

**Full commit:** `e97d44d65c6a1f5f4641650cad4d321e426d3f70`

Fix preview backup database role detection

- Detect Postgres database and role from the running preview container
- Keep explicit CODIQUIZ_DB_NAME and CODIQUIZ_DB_USER overrides
- Avoid hard-coding local development database defaults for preview backups
- Improve backup failure diagnostics for database readiness checks

## 2026-06-07 - `a2d34e5`

**Author:** Spiros Kontopoulos

**Full commit:** `a2d34e52c3f26a47d392d059d0b8a66f0c13871a`

Add preview backup foundation and runbooks

- Add a Docker Compose based Postgres backup script for preview
- Document manual restore, retention, and backup verification steps
- Add preview operations and smoke-test checklists
- Capture safe update, rollback, log review, and disk cleanup commands

## 2026-06-07 - `dce24e7`

**Author:** Spiros Kontopoulos

**Full commit:** `dce24e7877017044be73d075632244e49d1f467b`

Seed default Blueprint base rule

- Add an idempotent global Blueprint base rule seed
- Use target count 2 as the Codiquiz baseline
- Preserve existing active admin-created global rules
- Document why fresh deployments need the base rule for coverage expansion

## 2026-06-06 - `9fc01f8`

**Author:** Spiros Kontopoulos

**Full commit:** `9fc01f8ac5c52147680f079d7c993ea902e6ae92`

Use clean admin subdomain URLs

- Mount admin routes at the root when running on admin subdomains
- Keep local development admin routes under /admin unchanged
- Redirect legacy /admin paths on the admin hostname to clean equivalents
- Normalize admin login, navigation, demo restrictions, and back links

## 2026-06-06 - `3b58454`

**Author:** Spiros Kontopoulos

**Full commit:** `3b584540b198fc4943130aaffcd34dacce49da4a`

Clarify admin domain root redirect

- Use an explicit Caddy named matcher for the admin hostname root
- Keep admin.preview.codiquiz.com redirecting to the /admin SPA route
- Preserve public/admin hostname separation and API proxy behavior

## 2026-06-06 - `0ca51ef`

**Author:** Spiros Kontopoulos

**Full commit:** `0ca51ef2008e7d7261eb78fc835f20ec7869518a`

Redirect preview admin domain to admin app

- Redirect the admin hostname root to the /admin SPA route
- Correct preview and production deployment examples to use codiquiz.com
- Document the admin-domain routing behavior for the preview deployment
- Keep API proxying and frontend SPA fallback behavior unchanged

## 2026-06-06 - `a3fcf8f`

**Author:** Spiros Kontopoulos

**Full commit:** `a3fcf8f3af9d089efa2f14d2fed1d48c2e191007`

Support preview deployment domains

- Add preview environment template for isolated demo deployment
- Make Caddy public and admin site addresses configurable from env
- Require Vite API URL from the selected deployment env file
- Document preview versus production VPS separation and DNS requirements

## 2026-06-06 - `4226dc3`

**Author:** Spiros Kontopoulos

**Full commit:** `4226dc38572985b1b89ae5a17d188b5352d298fb`

Add production deployment foundation

- Add production Docker Compose, Caddy routing, and frontend production build templates
- Add production environment example and deployment checklist documentation
- Document manual deploy flow, migrations, verification, logs, and backup expectations
- Keep local development unchanged while separating production-only infrastructure settings

## 2026-06-06 - `6ebb844`

**Author:** Spiros Kontopoulos

**Full commit:** `6ebb8446f91d987ec2cc045ac84e0a2af2405b1e`

Refine public taxonomy visuals

- Calm the technology-page sidebar and stat-bar styling
- Improve sidebar icon contrast with purple tiles and white icons
- Use consistent soft-purple hover states for taxonomy navigation
- Keep topic/subtopic card icons colorful while standardizing card hover behavior
- Make practice links visually calmer and consistent with card titles

## 2026-06-06 - `ad5d3ac`

**Author:** Spiros Kontopoulos

**Full commit:** `ad5d3acc316c4939a08e16ae240cf9d882b15800`

Polish public site before deployment

- Add alpha notice modal and homepage banner
- Add How It Works page and redirect About route
- Load featured homepage quizzes from live quiz data
- Add Lucide taxonomy icons and clickable technology-page card polish
- Improve public homepage and technology smoke coverage

## 2026-06-06 - `670de83`

**Author:** Spiros Kontopoulos

**Full commit:** `670de83a985d068faeaa406d85eac51d735aec49`

Add deployment security checklist

- Add admin security readiness endpoint and checklist page
- Centralize production CORS and auth cookie security settings
- Disable Admin Test Lab by default in production environments
- Document pre-deployment security environment requirements
- Add E2E coverage for security checklist and demo blocking

## 2026-06-06 - `5c24645`

**Author:** Spiros Kontopoulos

**Full commit:** `5c246455aa1ec8c3b1d972518b3505859239d538`

Polish admin login credentials

- Add optional usernames for admin and demo users
- Allow admin login with either email or username
- Add password visibility controls to login and user-management forms
- Update Users / Access to create and edit usernames
- Update E2E demo auth to use username credentials

## 2026-06-06 - `b371f05`

**Author:** Spiros Kontopoulos

**Full commit:** `b371f05fb7c88a74e4b81a65fbd135d1de70e27d`

Add admin activity tracking

- Add admin activity events and current-page session tracking
- Track login, logout, and admin page-view activity
- Add heartbeat endpoint and online admin users view
- Add Admin Activity workspace and dashboard summary cards
- Add E2E smoke coverage for admin activity visibility

## 2026-06-06 - `c43805e`

**Author:** Spiros Kontopoulos

**Full commit:** `c43805e9ce470a1571337da9187f8c752a94dbcd`

Add public traffic location resolver

- Add privacy-safe public visit location resolver
- Support trusted proxy and CDN geo headers for production location detection
- Prepare optional MaxMind GeoIP2 lookup without requiring it locally
- Classify local Docker/private-network visits clearly
- Show location source and status in public tracking admin

## 2026-06-06 - `85b9209`

**Author:** Spiros Kontopoulos

**Full commit:** `85b92093d976a8a7430ffb71cdda02f9a5a43c84`

Add public visitor session tracking

- Add visitor-session table for public traffic analytics
- Track anonymous browser sessions with a 30-minute inactivity timeout
- Separate visitors, sessions, and page views in admin reporting
- Keep page-view events for behavior inspection
- Update dashboard and E2E smoke coverage for tracking semantics

## 2026-06-06 - `29bc4e4`

**Author:** Spiros Kontopoulos

**Full commit:** `29bc4e4e92573306ac910a4896d040e7cad384e7`

Harden public visitor IP tracking

- Add salted IP hash fields for public visit events
- Prepare country and city tracking from trusted proxy headers
- Keep raw IP storage disabled by default
- Show privacy-safe network and location data in public tracking admin
- Add migration for public visit IP and geo fields

## 2026-06-06 - `5d3c654`

**Author:** Spiros Kontopoulos

**Full commit:** `5d3c65465d353f392da58de61821a60f006abd8d`

Add public visitor tracking

- Track anonymous public page views with flexible src campaign keys
- Add public traffic source and visit event tables
- Add admin public tracking workspace with source labels and recent visits
- Show public traffic summary on the admin dashboard
- Add E2E smoke coverage for the tracking page

## 2026-06-06 - `138349f`

**Author:** Spiros Kontopoulos

**Full commit:** `138349f550a4177c9e0c757344c84ab09fe95a9c`

Polish demo restriction handling

- Add modal-based feedback for blocked demo actions
- Keep restricted page behavior for direct blocked route access
- Fix forbidden response handling so demo blocks do not appear as failed fetch
- Add CORS-safe handling for early 401 and 403 auth responses
- Stabilize TypeScript build after restriction modal changes

## 2026-06-05 - `d20f1be`

**Author:** Spiros Kontopoulos

**Full commit:** `d20f1be967a6592fc2dc2e632484f5ec35061953`

Add demo permissions and admin logout

- Add global admin logout and session toolbar
- Enforce demo-viewer read-only restrictions in backend middleware
- Block known dangerous admin routes for demo users
- Keep public quiz-attempt routes open while protecting quiz-management mutations
- Add E2E coverage for demo restrictions and logout visibility

## 2026-06-05 - `a4352e5`

**Author:** Spiros Kontopoulos

**Full commit:** `a4352e59155a6e28b9c9d435fadd7ca36879fd61`

Add admin user management

- Add owner-only admin users API
- Add Users / Access admin workspace
- Support user creation, role changes, enable/disable, and password reset
- Add authenticated admin fetch helper for user-management requests
- Add E2E smoke coverage for the access page

## 2026-06-05 - `ca4aa37`

**Author:** Spiros Kontopoulos

**Full commit:** `ca4aa3725b600a2f815f4644248f59bd36d05772`

Add admin auth foundation

- Add admin users and auth session models with migration
- Add login, logout, and current-user admin auth endpoints
- Protect admin frontend routes and protected admin API prefixes
- Add first-owner creation helper and E2E login support

## 2026-06-05 - `b782cb1`

**Author:** Spiros Kontopoulos

**Full commit:** `b782cb1224231e58b61b94000bab5078881d9e37`

Stabilize Quick Practice E2E start flow

- Wait for the Practice session page as the primary user-visible success condition
- Keep POST /practice-sessions status validation when the response is observed
- Make the broad-module start test more reliable during the full parallel E2E suite

## 2026-06-05 - `76289fc`

**Author:** Spiros Kontopoulos

**Full commit:** `76289fcfc97af189f7e2847ff49686941232cd02`

Add Developer Tools cleanup for E2E generation batches

- Add safe Admin Test Lab endpoint to preview and archive marked E2E AI generation batches
- Add Developer Tools UI controls for manual cleanup with marker and age guard
- Archive matching batches instead of deleting them
- Mark Playwright-created generation batches with an explicit E2E cleanup marker
- Document the cleanup flow for interrupted or failed E2E runs

## 2026-06-05 - `b35c8c0`

**Author:** Spiros Kontopoulos

**Full commit:** `b35c8c0c3b9d9ff960444e2af6dab68414b7aa0e`

Add Playwright smoke tests for Blueprint generation flow

- Cover Blueprint workspace cards and filters
- Cover Normal mode per-row difficulty and gap preview behavior
- Cover Blueprint Assist create-batch regression for the prior 422 error
- Cover Reverse mode exploration settings without global difficulty
- Archive E2E-created batches after each test to keep active queues cleaner

## 2026-06-05 - `378aeef`

**Author:** Spiros Kontopoulos

**Full commit:** `378aeeff4bffa0bd558043a89f826211e066f146`

Fix Blueprint Assist manual plan validation

- Allow explicit manual plan items to validate from their per-row taxonomy identity
- Stop requiring Blueprint Assist rows to collapse into one top-level domain/module scope
- Keep plan items restricted to manual allocation
- Preserve distributed allocation validation for non-manual create requests

## 2026-06-05 - `1f96731`

**Author:** Spiros Kontopoulos

**Full commit:** `1f9673146e2ef8d5e04459f20e28351e0fd3b6f8`

Add Blueprint alignment labels to AI drafts

- Store Blueprint alignment status on generated AI draft questions
- Classify drafts as gap fill, expansion, over-cap, outside target, or needs mapping review
- Recompute alignment after reverse-mode concept mapping review
- Show Blueprint alignment labels in batch detail and draft review inbox

## 2026-06-05 - `1ac9a42`

**Author:** Spiros Kontopoulos

**Full commit:** `1ac9a42511fded899fa1ca24816842f5124bd293`

Use Blueprint gaps for Normal mode planning

- Change Normal mode requested count into a batch safety cap
- Require preview plan before creating Normal mode batches
- Default planned row counts from Blueprint effective gaps
- Send edited preview rows as the manual generation plan
- Keep Reverse mode count behavior unchanged for now

## 2026-06-05 - `46f431c`

**Author:** Spiros Kontopoulos

**Full commit:** `46f431c73395e63744d3d7a37b9515871396d758`

Redesign Normal mode difficulty selection

- Move Normal mode difficulty selection into Step 5 per question-type row
- Replace global Normal mode difficulty controls with compact per-cell difficulty summaries
- Add an expandable difficulty editor for selected question types
- Keep recommended and allowed difficulty states visible without widening the table
- Update preview override totals so edited plans create with the adjusted count

## 2026-06-05 - `99c4096`

**Author:** Spiros Kontopoulos

**Full commit:** `99c40968a11e18b845637071c0ae723d1a59d70d`

Stabilize AI generation difficulty guidance

- Preserve difficulty eligibility metadata in suitability rule creation
- Keep AI Generation Create difficulty guidance and blocker behavior stable
- Keep target metric layout and candidate pagination compatibility fixes
- Prepare for the next Normal mode generation-planning redesign

## 2026-06-05 - `d6845fb`

**Author:** Spiros Kontopoulos

**Full commit:** `d6845fbaa3d719ff93b3bcc080c8d0f8ff71597c`

Clarify blueprint workspace filtering

- Make Blueprint workspace cards the only clickable view selectors
- Convert Blueprint work queue cards into read-only snapshot stats
- Move suitability tier selection into the normal filter panel
- Prevent hidden queue-card filtering and reduce accidental repeated requests

## 2026-06-05 - `18a38c2`

**Author:** Spiros Kontopoulos

**Full commit:** `18a38c2de47b2a407d40188788634c1abd4f70f4`

Reorganize blueprint admin workspace

- Add focused Blueprint workspace blocks for default targets, coverage rows, and generation candidates
- Stop rendering all Blueprint workflows at once on the same page
- Add pagination to the default target preview workflow
- Move generation candidates out of the main filter-to-rows flow

## 2026-06-05 - `b5ceeff`

**Author:** Spiros Kontopoulos

**Full commit:** `b5ceeff0ea24cf480b0449f6a803fd368b6c2550`

Add blueprint default target review UI

- Add frontend API support for Blueprint default target preview
- Show active policy mode and target summary on the Blueprint page
- Display selected target rows with difficulty eligibility and rationale
- Prepare the admin UI for a fuller Blueprint review workflow

## 2026-06-05 - `0d8ed42`

**Author:** Spiros Kontopoulos

**Full commit:** `0d8ed422aefbcdfe23e7e5e34cd0c72e152a68b4`

Add blueprint target rules and difficulty eligibility

- Add hard difficulty eligibility flags to suitability rules
- Seed conservative, normal, and expansion Blueprint target-budget rules
- Block invalid difficulties from automatic default-target selection
- Recalculate default Blueprint targets from active policy settings

## 2026-06-04 - `7b1df3f`

**Author:** Spiros Kontopoulos

**Full commit:** `7b1df3ffaee625e04a4e67975b690436fc423b8f`

Add blueprint default target preview

- Add read-only default target preview endpoint
- Combine concept importance, suitability, difficulty fit, and current coverage
- Limit automatic targets to strong or high-secondary reviewed suitability
- Add per-concept target budgets to avoid generating every suitable cell

## 2026-06-04 - `92f8fbb`

**Author:** Spiros Kontopoulos

**Full commit:** `92f8fbb8c736f5665dbd2542f8e1ec7a915eef08`

Optimize blueprint coverage suitability lookup

- Avoid scanning all suitability rows for every blueprint coverage cell
- Build a source-aware suitability index for blueprint scoring
- Prefer reviewed suitability mappings over fallback taxonomy seed rows
- Run heavy blueprint endpoints as sync routes to avoid blocking the API event loop

## 2026-06-04 - `cec06c2`

**Author:** Spiros Kontopoulos

**Full commit:** `cec06c2f351a67c5e497cddeebedf24f92e7240d`

Treat legacy suitability seed rows as reviewed

- Count legacy Lists pilot seed rows as reviewed suitability
- Reserve taxonomy_seed rows for fallback autogenerated coverage
- Fix false positives in reviewed strong-fit audit queues
- Keep suitability quality checks aligned with reviewed mapping sources

## 2026-06-04 - `7578302`

**Author:** Spiros Kontopoulos

**Full commit:** `7578302f6482d3b19625d9216a00ecdde487ac31`

Add suitability quality audit checks

- Distinguish reviewed suitability from fallback coverage
- Add quality queues for weak, missing, and overly broad suitability mappings
- Surface reviewed versus fallback coverage in the suitability audit page
- Update Coverage Audit compatibility with expanded suitability queues

## 2026-06-04 - `4b489ba`

**Author:** Spiros Kontopoulos

**Full commit:** `4b489bab8775994f73fd48f900804c0b654f10ba`

Add reviewed Python suitability mappings

- Add explicit concept-to-profile suitability mappings across Python taxonomy
- Keep autogenerated suitability as fallback for uncovered concepts
- Seed reviewed mappings with a distinct taxonomy_seed_reviewed source
- Override stale fallback rows when reviewed profiles exist

## 2026-06-04 - `325d367`

**Author:** Spiros Kontopoulos

**Full commit:** `325d367ed84625b48f6572ad4e42f79f7cde1919`

Add Python concept suitability seed baseline

- Add direct concept-level question-type suitability seeding
- Cover active Python concepts with deterministic baseline recommendations
- Add domain profiles for Core Language, Advanced Python, and OOP
- Prepare suitability coverage for Blueprint default generation

## 2026-06-04 - `e60718f`

**Author:** Spiros Kontopoulos

**Full commit:** `e60718ff65675404d9df20535e6cc963d076f6f7`

Add question type suitability audit page

- Add dedicated admin page for suitability coverage audit
- Link suitability management and Coverage Audit to the audit page
- Show suitability coverage queues and taxonomy-filtered review results
- Keep Coverage Audit focused on compact suitability coverage

## 2026-06-04 - `18a41f6`

**Author:** Spiros Kontopoulos

**Full commit:** `18a41f6037d2fe41f3455c626fbee0dca5c62f37`

Add concept importance admin page

- Add dedicated admin page for concept importance review
- Move queue results and analytics out of Coverage Audit
- Keep Coverage Audit focused on compact importance coverage
- Add admin navigation and route for the importance page

## 2026-06-04 - `dd8735f`

**Author:** Spiros Kontopoulos

**Full commit:** `dd8735fc90e8cfa999bb3c67de7f477b0026aab8`

Cover legacy concepts with importance metadata

- Add importance metadata for legacy seeded concepts
- Upsert concept_importance rows from legacy seed_data concepts
- Close the remaining missing importance coverage gap
- Bring active concept importance coverage to 100%

## 2026-06-04 - `dbbf224`

**Author:** Spiros Kontopoulos

**Full commit:** `dbbf2244173a57a6fa1fd1e446993dbea9e185ff`

Add concept importance audit visibility

- Add taxonomy audit endpoint for concept importance review
- Show scored, missing, and tiered concept queues
- Add module and topic importance distributions
- Add admin coverage visibility for importance scoring

## 2026-06-04 - `151aeea`

**Author:** Spiros Kontopoulos

**Full commit:** `151aeea5d719201cbed76c4a3ee535af2816fe04`

Add inline concept importance seed metadata

- Extend concept seed declarations with inline importance scores
- Upsert concept_importance rows from taxonomy seeding
- Derive importance tiers from score ranges
- Add baseline scores across Python taxonomy concepts

## 2026-06-04 - `fb979dc`

**Author:** Spiros Kontopoulos

**Full commit:** `fb979dc271e10d9e3fc9dc7a17c5edfae943bb0c`

Add concept importance model

- Add concept_importance table and migration
- Add one-to-one concept importance relationship
- Add Pydantic schemas for future admin/API use
- Enforce importance tiers and score range

## 2026-06-04 - `e6deb56`

**Author:** Spiros Kontopoulos

**Full commit:** `e6deb56a5acc70bc370905579c9c6835436d7fa5`

Expand Python OOP taxonomy

- Add Object-Oriented Programming seed coverage across modules, topics, subtopics, and concepts
- Use the existing oop domain slug to avoid duplicate active domains
- Archive the accidental duplicate object-oriented-programming domain
- Bring OOP into the quality-filtered target range for mature Python coverage

## 2026-06-04 - `748f50b`

**Author:** Spiros Kontopoulos

**Full commit:** `748f50bc1ea06fc03cdfe57ce29892e3b938b2c5`

Expand Python Advanced Python taxonomy

- Add Advanced Python seed coverage across modules, topics, subtopics, and concepts
- Cover closures, generators, decorators, context managers, async language features, descriptors, metaprogramming, and related advanced areas
- Bring Advanced Python into the quality-filtered target range for mature Python coverage
- Preserve the field-aware topic-file seed structure

## 2026-06-04 - `81923d4`

**Author:** Spiros Kontopoulos

**Full commit:** `81923d4c4066a9d95d05a6c1cb245621d3548cb3`

Expand Python Core Language taxonomy

- Add broad Core Language seed coverage across modules, topics, subtopics, and concepts
- Raise Core Language concept coverage into the quality-filtered mature range
- Preserve field-aware seed module structure for future Python domain expansion

## 2026-06-04 - `7ceb7a8`

**Author:** Spiros Kontopoulos

**Full commit:** `7ceb7a8f854a63ce24ab10c6e5e9b7c05fadcab1`

Allow flexible concept anchoring

- Keep concept identity mandatory for approved questions
- Allow concepts to belong directly to topics when no subtopic is needed
- Require matching subtopic only when the selected concept is subtopic-anchored
- Preserve strict rejection of broad topic-only question targets

## 2026-06-04 - `bfad5e2`

**Author:** Spiros Kontopoulos

**Full commit:** `bfad5e255658b11dc30eb4717861b76b8d456627`

Organize Python taxonomy seed modules

- Add field-aware seed module layout for technology taxonomy
- Place Python under the programming languages field hierarchy
- Split Data Structures taxonomy into topic-level seed files
- Keep existing seed entrypoint compatible while enabling future taxonomy expansion

## 2026-06-03 - `0b8fcac`

**Author:** Spiros Kontopoulos

**Full commit:** `0b8fcacb57b398a69be18188ac4c20c90fefce1f`

Complete reverse generation normalization

- Hydrate full taxonomy paths when reverse classifications are applied
- Enforce subtopic and concept relationships before AI draft approval
- Retry OpenAI responses once when generated answer options fail validation
- Strengthen prompt rules for unique answer option text

## 2026-06-03 - `e945f96`

**Author:** Spiros Kontopoulos

**Full commit:** `e945f967dd790d7a6f730351f140657ce8535a2d`

Harden generation taxonomy target selection

- Require strict concept-level targets for normal generation mode
- Preserve broad target behavior for reverse mode
- Expand reverse-mode plan items by selected question types
- Add backend guards against incomplete taxonomy approval/manual creation

## 2026-06-03 - `977e06b`

**Author:** Spiros Kontopoulos

**Full commit:** `977e06b4431d1d0c0aa95fb9fa6a67c33f14f4ec`

Polish admin question search filters

- Add exact Question ID filtering to shared question search UI
- Rename full-text search to Question content
- Add ID visibility and shared pagination to quiz question picker
- Tighten Question ID layout inside the shared filter panel

## 2026-06-03 - `a5b6d66`

**Author:** Spiros Kontopoulos

**Full commit:** `a5b6d66ca14a1b4a4e50640d151bf6c587143384`

Polish worker task history visibility

- Add worker task history filters in AI Generation Settings
- Use shared admin filter panel for worker history filters
- Improve failed task visibility and filtered empty states
- Add stronger batch tagging for lifecycle worker task runs

## 2026-06-03 - `44352e2`

**Author:** Spiros Kontopoulos

**Full commit:** `44352e22d22620a0a25dba8d1292bd698adfe07d`

Add section blocks to AI generation detail page

- Add clickable section blocks for batch history, execution jobs, plan items, and drafts
- Show one focused detail section at a time
- Add execution job pagination using the shared admin pagination component
- Align section block labels with the admin settings pattern

## 2026-06-03 - `ca065bd`

**Author:** Spiros Kontopoulos

**Full commit:** `ca065bd8c152d8e193224caeac59d4d0698591e1`

Show per-batch worker task history

- Add batch-scoped worker task-run API endpoint
- Display Batch automation history on AI Generation Detail
- Reuse worker task-run pagination model from Settings
- Add frontend API helper and detail-page pagination state

## 2026-06-03 - `f0c4719`

**Author:** Spiros Kontopoulos

**Full commit:** `f0c4719de1b971fd7b99a3b888ac73824aa78a29`

Update Codiquiz documentation for alpha and user systems

- Add early alpha status and user accounts/progress documentation.
- Expand vocabulary for taxonomy, Blueprint, AI generation, similarity, attempts, ranking, and mastery.
- Add deeper AI generation workflow notes for prompt rules, provider output, chunking, and retries.
- Expand Blueprint coverage docs with rules, row status, and candidate selection.

## 2026-06-03 - `afcccda`

**Author:** Spiros Kontopoulos

**Full commit:** `afcccda9c682714e8e6b11c55167258a22bad52e`

Update README.md

## 2026-06-03 - `e6dcbdf`

**Author:** Spiros Kontopoulos

**Full commit:** `e6dcbdf2bd1ae6298ba8813999c97c755f65e2e4`

Add Codiquiz architecture documentation

- Add public-facing README for Codiquiz product and architecture positioning.
- Document AI generation, Backend Quality Engine, Blueprint coverage, suitability mapping, and async automation.
- Add roadmap docs for GraphQL, embeddings, serving, scoring, ranking, and deployment.
- Include architecture and AI generation lifecycle diagrams.

## 2026-06-03 - `677d0be`

**Author:** Spiros Kontopoulos

**Full commit:** `677d0bee7d596319a1b061bac767e635a1d85872`

Paginate worker task history in admin settings

- Add paginated worker task-run history to the AI Generation Settings API.
- Support worker task-run limit and offset query parameters.
- Reuse AdminPagination for the Recent worker task runs section.
- Add rows-per-page and page navigation for async worker history.

## 2026-06-03 - `2f8902c`

**Author:** Spiros Kontopoulos

**Full commit:** `2f8902c365cbac14baed8b340e860e844fb8519c`

Show worker task history in admin settings

- Add recent worker task-run history to the AI Generation Settings response.
- Show recent async worker runs in the Redis/Celery settings section.
- Display task name, status, action, target batch, dry-run mode, duration, and errors.
- Provide first admin visibility layer for scheduled Batch API automation.

## 2026-06-03 - `6fed5a6`

**Author:** Spiros Kontopoulos

**Full commit:** `6fed5a675e6207fc351b7611fcbd98f4556950ab`

Add worker task run logging

- Add worker_task_runs table and SQLAlchemy model for async task history.
- Add worker task-run logging helper for start, success, and failure tracking.
- Record Batch API lifecycle scanner task runs with status, dry-run flag, and duration.
- Extend async self-check notes to confirm ASYNC 3 visibility foundation.

## 2026-06-03 - `d4b769e`

**Author:** Spiros Kontopoulos

**Full commit:** `d4b769ef39cacb95d09b3cbb7fa9ceeefa6f0582`

Normalize generated draft question text

- Strip duplicated fenced code blocks from generated question prompts when code snippets are stored separately.
- Extract fenced code into code_snippet when the provider puts code only inside question text.
- Apply the normalization in the shared draft storage path for both Normal API and Batch API generations.
- Prevent review UI drafts from showing the same code in both prompt text and code block.

## 2026-06-03 - `f922497`

**Author:** Spiros Kontopoulos

**Full commit:** `f922497dc3357177ddb3c4d9598d10887555ef60`

Clarify Batch API automation UI wording

- Add Batch API automation notice to the generation detail lifecycle panel.
- Clarify that lifecycle buttons remain manual override and debug actions.
- Reword Redis/Celery settings as a read-only configuration snapshot.
- Avoid implying admin-editable automation controls before DB-backed settings exist.

## 2026-06-03 - `47185c9`

**Author:** Spiros Kontopoulos

**Full commit:** `47185c9b7db13eb09cd657e6c2302df6387b9a38`

Add Batch API automation controls

- Expose scheduled Batch API lifecycle automation status in AI Generation Settings.
- Add scanner interval, limit, and dry-run visibility for safer operation.
- Document Batch API scanner environment settings.
- Keep scheduled automation configurable while preserving manual admin controls.

## 2026-06-03 - `cf47031`

**Author:** Spiros Kontopoulos

**Full commit:** `cf47031ae8bd14b6844263cea8dddd7871fce726`

Schedule Batch API lifecycle scanner

- Add a Celery Beat schedule for bounded Batch API lifecycle scanner passes.
- Run automated lifecycle scans with a safe per-pass batch limit.
- Expose scanner schedule and limit in AI Generation Settings readiness.
- Move Celery Beat runtime schedule storage out of the source tree.
- Ignore Celery Beat runtime state files to keep Git status clean.

## 2026-06-03 - `f370f8a`

**Author:** Spiros Kontopoulos

**Full commit:** `f370f8aa75fe3297ad70249cd5f4d9fa1deb70db`

Add Batch API lifecycle scanner task

- Add a Celery scanner task that discovers Batch API batches needing lifecycle progress.
- Support dry-run candidate discovery before processing real batches.
- Skip archived, normal API, terminal, and already reconciled batches safely.
- Reuse existing lifecycle worker orchestration for status polling, collection, and reconciliation.
- Extend async self-check notes to confirm scanner readiness.

## 2026-06-03 - `aa3ac56`

**Author:** Spiros Kontopoulos

**Full commit:** `aa3ac5696d1c42199cfaf0d660150d97da35db68`

Add Batch API lifecycle worker tasks

- Add Celery tasks for Batch API status polling, result collection, draft reconciliation, and lifecycle orchestration.
- Reuse existing Batch API lifecycle guards so worker actions stay idempotent and safe.
- Keep automation manually testable only; scheduled Batch API scanning remains planned for the next ASYNC step.
- Extend async self-check notes to confirm Batch API worker task availability.

## 2026-06-03 - `cafa410`

**Author:** Spiros Kontopoulos

**Full commit:** `cafa4103b251116039081df4d0225d70dfddde62`

Complete ASYNC 1 Redis Celery foundation

- Add quiz-api Celery worker and Celery Beat scheduler foundation.
- Confirm Redis broker/result backend readiness for quiz-api background jobs.
- Add worker health and scheduled heartbeat tasks for async smoke validation.
- Expose ASYNC 1 Redis/Celery readiness in AI Generation Settings.
- Keep Batch API automation planned for ASYNC 2 while preserving manual admin controls.

## 2026-06-03 - `0e6121b`

**Author:** Spiros Kontopoulos

**Full commit:** `0e6121bc97c4c543910f7f1887143a3eead4295f`

Add Redis Celery foundation for quiz API

- Add quiz-api owned Celery worker foundation for product/database workflows.
- Add Redis/Celery config, worker health task, and async readiness self-check.
- Expose Redis and Celery readiness in AI Generation Settings.
- Keep question-service worker focused on provider and prompt boundaries.

## 2026-06-02 - `1b28fa0`

**Author:** Spiros Kontopoulos

**Full commit:** `1b28fa05f775002b220e5493caa435665fc4410d`

Complete Batch API final hardening

- Prevent invalid Batch API lifecycle actions after collection or reconciliation.
- Add clearer disabled reasons for submit, status, collect, and reconcile actions.
- Harden archived/non-Batch API safeguards for Batch API write actions.
- Update Batch API readiness smoke coverage for the current settings UI.

## 2026-06-02 - `f637820`

**Author:** Spiros Kontopoulos

**Full commit:** `f63782008beee3d1e7b2a06f077fed2527e7aa04`

Polish AI generation batch mode filters

- Add a separate execution mode filter for Normal API and Batch API
- Simplify generation status filtering into cleaner lifecycle states
- Show Normal API and Batch API mode chips in the batches list
- Remove noisy lifecycle text from the main status column

## 2026-06-02 - `6bff64a`

**Author:** Spiros Kontopoulos

**Full commit:** `6bff64a373331f65669ba5c8d9b218c00ebdb11e`

Polish Batch API detail layout

- Move Batch API lifecycle controls into a full-width section
- Keep Gen AI execution and cost as the shared compact card
- Show Batch API lifecycle only for Batch API batches
- Improve spacing and alignment on AI generation detail pages

## 2026-06-02 - `62deb0e`

**Author:** Spiros Kontopoulos

**Full commit:** `62deb0efe93c3adfecb86a7291338531d527d535`

Polish Batch API lifecycle display

- Add Batch API lifecycle stepper on generation detail pages
- Clarify Batch API action labels and next-action hints
- Update AI Generation Settings to show the lifecycle as ready
- Improve Batch API status copy after submit, collect, and reconcile

## 2026-06-02 - `51c2a82`

**Author:** Spiros Kontopoulos

**Full commit:** `51c2a82bd2014612adf56c438a7363c64d5043dc`

Fix cross-batch duplicate canonical sources

- Allow same-concept duplicate matching across question types for live pending drafts
- Keep archived approved questions from blocking future duplicate checks
- Let the oldest live pending draft become the canonical duplicate source
- Show archived status beside approved question links in AI draft review

## 2026-06-02 - `4a9957a`

**Author:** Spiros Kontopoulos

**Full commit:** `4a9957a2720d3e5e685bc3ffc67e52b8eb5a92c1`

Preserve approved question duplicate sources

- Keep same-concept strong matches blocking after canonical drafts are approved
- Downgrade only different-concept strong prompt/code matches to related-pattern notes
- Expand approved-question candidate scope for same-concept duplicate checks
- Fix duplicate self-check coverage for same-concept and related-pattern severity

## 2026-06-02 - `38e4d0f`

**Author:** Spiros Kontopoulos

**Full commit:** `38e4d0fe68817b90f932fc650635a579fefe5de1`

Refresh duplicate warnings after review decisions

- Recompute duplicate notes after bulk review decisions
- Refresh pending draft warnings after individual approve or reject actions
- Let the existing admin AJAX refetch show updated duplicate status immediately
- Keep the refresh scoped to the current batch

## 2026-06-02 - `f45c72e`

**Author:** Spiros Kontopoulos

**Full commit:** `f45c72e24855c8705fa07d64c8f729455c5a1311`

Use canonical duplicate draft sources

- Prefer active approved question-bank rows over AI draft duplicate sources
- Limit AI draft duplicate checks to older live pending drafts
- Collapse draft duplicate warnings to the oldest canonical draft source
- Add self-check coverage for canonical draft duplicate selection

## 2026-06-02 - `e68295d`

**Author:** Spiros Kontopoulos

**Full commit:** `e68295d1a8cf025236f2b049397fae6319405ee6`

Downgrade cross-concept pattern matches

- Keep exact and same-target matches as hard duplicate warnings
- Downgrade similar cross-concept patterns to informational related-pattern notes
- Refresh related-pattern notes during duplicate-warning sync
- Show related-pattern notes as non-blocking labels in AI generation review

## 2026-06-02 - `21118c6`

**Author:** Spiros Kontopoulos

**Full commit:** `21118c655a64afaf35b32662c6078fd332d2b4eb`

Reconcile Batch API results into AI drafts

- Add Batch API reconciliation action for collected provider results
- Create staged AI drafts from collected OpenAI Batch API responses
- Reuse validation, signature, pattern, and duplicate-warning pipeline for reconciled drafts
- Update execution jobs, plan items, and batch generated counts after reconciliation
- Show successful collection and reconciliation messages as status instead of errors

## 2026-06-02 - `9fdca33`

**Author:** Spiros Kontopoulos

**Full commit:** `9fdca33a1a870a84e7bd83a16d112bbc5be6b20b`

Collect Batch API provider results

- Add provider response/error storage for Batch API execution jobs
- Download and parse Batch API output/error JSONL files through question-service
- Match collected result lines back to execution jobs by custom_id
- Add admin collection action and Batch API collection lifecycle labels

## 2026-06-02 - `f757865`

**Author:** Spiros Kontopoulos

**Full commit:** `f757865a7dc1b307c0655abf3878e1a380e4c14f`

Add Batch API submit and status tracking

- Add provider batch/file/custom-id tracking fields
- Submit prepared Batch API jobs to OpenAI through question-service
- Add provider status polling and Batch API lifecycle labels
- Expose Batch API provider metadata in admin detail and list pages

## 2026-06-02 - `d404460`

**Author:** Spiros Kontopoulos

**Full commit:** `d40446030f982da65443d33dd13a64478b1a0c8c`

Limit duplicate checks to active sources

- Exclude archived AI batches from draft duplicate-source lookup
- Exclude approved and non-pending AI drafts from draft duplicate-source lookup
- Hide archived-batch drafts from global Similarity Review queues and clusters
- Clear duplicate-warning text when archived batches are synced

## 2026-06-02 - `bf133b8`

**Author:** Spiros Kontopoulos

**Full commit:** `bf133b84ed7303dfb1eceb111c29ffd95d20c7d6`

Reserve Blueprint gaps only with clean pending drafts

- Keep pending review drafts in effective Blueprint gap calculations
- Exclude taxonomy-review drafts from pending gap reservations
- Exclude drafts with validation or duplicate warnings from reservation counts
- Prevent unsafe drafts from hiding actionable Blueprint gaps

## 2026-06-02 - `30bd2d5`

**Author:** Spiros Kontopoulos

**Full commit:** `30bd2d55c909a5d6d0cd0088b1f4f7aceda2c750`

Add Batch API execution mode foundation

- Add normal_api and batch_api execution mode handling
- Prepare Batch API execution jobs without submitting to OpenAI yet
- Add execution mode selector and Batch API prepared status in admin UI
- Stabilize AI generation smoke test question-type selection

## 2026-06-02 - `259e2ae`

**Author:** Spiros Kontopoulos

**Full commit:** `259e2ae9405926c9fc856549931c3063a86cc07c`

Fix recent admin smoke card selectors

- Match focused card buttons by inner title text more flexibly
- Restore Similarity Review, Settings, Draft Inbox, and Coverage Audit smoke coverage
- Keep shared recent-admin smoke helpers reusable

## 2026-06-02 - `ee167ca`

**Author:** Spiros Kontopoulos

**Full commit:** `ee167ca8f82fa5dbf351fb7d06dd2e95c4a4d5bb`

Add AI generation settings inspector

- Add read-only admin settings page for AI generation configuration
- Expose model profile and prompt rules metadata from backend services
- Show provider mode and Batch API readiness sections
- Add settings navigation and smoke coverage

## 2026-06-02 - `e21410e`

**Author:** Spiros Kontopoulos

**Full commit:** `e21410ece3a921f36181f0f8f0bb4bf35ac2bab4`

Add compact AI generation avoid-list support

- Build capped avoid-list entries from previous drafts in the same plan item
- Send compact avoid_patterns to question-service without full prior question payloads
- Add prompt rules for using avoid patterns as negative examples
- Keep post-generation duplicate warnings active

## 2026-06-01 - `9058d82`

**Author:** Spiros Kontopoulos

**Full commit:** `9058d820592629115159dc8f6a56edc28a11af8c`

Clarify AI generation batch status and review progress

- Display generation statuses with admin-friendly labels
- Move generation mode out of the status cell and into model details
- Rename counts to drafts and show labelled review progress
- Add review-state filtering to the AI generation batches page

## 2026-06-01 - `596f834`

**Author:** Spiros Kontopoulos

**Full commit:** `596f83450edc22f022dec9238f2392fa03206793`

Polish AI generation batch filters

- Add shared admin filters to the AI generation batches page
- Support field, technology, status, model, repetition, and archive filters
- Add result summary chip and technology-first plan labels
- Keep repetition rate visible first and sortable

## 2026-06-01 - `ca5502e`

**Author:** Spiros Kontopoulos

**Full commit:** `ca5502e8f6bd0fba5e57fdb61649abf07b78ef53`

Archive AI generation batches

- Add archive and restore support for AI generation batches
- Hide archived batches from the default active batch list
- Add Active, Archived, and All archive filters
- Add batch selection with archive/restore confirmation flow

## 2026-06-01 - `d90550d`

**Author:** Spiros Kontopoulos

**Full commit:** `d90550df837f14c26b929cf7960c6a6632eebeeb`

Add batch repetition summary

- Add anti-repetition summary service for AI generation batches
- Show repetition rate, affected drafts, repeated patterns, and warning counts
- Add sortable Repetition column to the AI generation batches page
- Reuse duplicate-warning data to measure batch generation quality

## 2026-06-01 - `ef4fda1`

**Author:** Spiros Kontopoulos

**Full commit:** `ef4fda1fc2b85edad97fd32a47bc433df4232a4c`

Harden answer-order duplicate policy

- Treat answer-option order as non-meaningful question identity
- Extend signature and duplicate self-checks for answer-order-only variants
- Document that serving-time shuffling handles answer order variation
- Update question-service prompt rules to discourage answer-order-only variants

## 2026-06-01 - `779bdbe`

**Author:** Spiros Kontopoulos

**Full commit:** `779bdbec71acffe3fc06fca0e3a7e9db84335462`

Shuffle answer options at serving time

- Add question_serving subsystem for public answer-option payload behavior
- Shuffle answer options deterministically for quiz and practice serving
- Keep database answer option order unchanged for admin and review flows
- Preserve answer submission correctness by using answer option IDs

## 2026-06-01 - `2865ea7`

**Author:** Spiros Kontopoulos

**Full commit:** `2865ea7df1cbdda5fec3e409049abe432572dbc9`

Add recent admin page Playwright smoke checks

- Add smoke coverage for recently polished admin pages
- Verify Similarity Review, Draft Review Inbox, Coverage Audit, Suitability, Enrichment, and Questions load
- Check focused mode switches and shared filter availability
- Stabilize selectors around queue-card titles instead of brittle full button text

## 2026-06-01 - `ca26c62`

**Author:** Spiros Kontopoulos

**Full commit:** `ca26c6292727dd6dc504e07820ecea12eef6628c`

Update admin AI generation Playwright smoke tests

- Align generation create tests with the current suitability-aware question type flow
- Select question type cells across target pages before applying selections
- Stabilize draft edit and approval checks after duplicate-warning validation
- Remove brittle assertions tied to older AI generation detail table layout

## 2026-06-01 - `bbca5b2`

**Author:** Spiros Kontopoulos

**Full commit:** `bbca5b29eca9cc4008596a40a696328f3b09eb2a`

Clarify question type suitability admin page

- Split the page into Manage rules and Resolve recommendations modes
- Replace custom rule filters with the shared admin filter panel
- Add taxonomy-aware filtering and result summary chip for suitability rules
- Explain inheritance preview behavior for resolved recommendations

## 2026-06-01 - `23f74c0`

**Author:** Spiros Kontopoulos

**Full commit:** `23f74c02e906471274a2f298a89c8070e58bfb28`

Focus taxonomy audit page sections

- Add focused section selectors for Coverage Audit
- Show coverage overview, audit diagnostics, or suitability review one at a time
- Reduce page density without removing existing audit functionality
- Keep nested audit and suitability queue filters inside their focused sections

## 2026-06-01 - `be0d591`

**Author:** Spiros Kontopoulos

**Full commit:** `be0d5915176793e80719e174859530836e8d0355`

Harden shared admin filter dropdown styling

- Keep selected filter values truncated with ellipsis
- Prevent long taxonomy names from resizing filter fields
- Remove hover gap between filter trigger and dropdown menu
- Apply the shared dropdown behavior across admin filter panels

## 2026-06-01 - `64269a3`

**Author:** Spiros Kontopoulos

**Full commit:** `64269a31d441fe4f83fbbc2c9f8da8c7b841d7c8`

Polish taxonomy audit admin filters

- Replace custom taxonomy audit controls with the shared admin filter pattern
- Add result summary chip, loading state, and queue-card affordance polish
- Keep audit and suitability queues focused with consistent admin styling
- Fix derived queue totals and coverage metrics after the layout update

## 2026-06-01 - `fb90faf`

**Author:** Spiros Kontopoulos

**Full commit:** `fb90faff4674e0fd8c02464a1626fc85bd683846`

Polish concept enrichment admin filters

- Replace custom filters with the shared admin filter panel
- Add taxonomy-aware filtering and result summary chip
- Improve queue-card selected/clickable states
- Add clearer loading behavior for Concept Enrichment

## 2026-06-01 - `816f145`

**Author:** Spiros Kontopoulos

**Full commit:** `816f145785c06c676371e63e43c3e6fbcd0de8c7`

Normalize admin filter result summaries

- Reuse the Blueprint-style result chip across admin filter panels
- Remove duplicated showing-range text from top filter rows
- Keep contextual result labels for Similarity Review and Draft Review Inbox
- Align Questions, Blueprint, Draft Review Inbox, and Similarity Review filter UX

## 2026-06-01 - `f854591`

**Author:** Spiros Kontopoulos

**Full commit:** `f85459185fdb73327a822f56941b2388cc052f9a`

Polish admin filter and review UI consistency

- Add shared filter result summaries to admin list pages
- Convert AI Draft Review Inbox to taxonomy-aware filtering
- Improve loading states for review/list pages
- Clarify clickable queue-card and metric-card behavior

## 2026-06-01 - `cd9cb0b`

**Author:** Spiros Kontopoulos

**Full commit:** `cd9cb0b017bd6c7762a6b7058af25b6603647d9a`

Add compact duplicate summaries to draft review

- Show duplicate warning counts on AI generation draft rows
- Add compact duplicate summary cards inside draft previews
- Surface duplicate summaries in the AI Draft Review Inbox
- Link affected drafts back to Similarity Review

## 2026-06-01 - `944481a`

**Author:** Spiros Kontopoulos

**Full commit:** `944481a0b8d048467d8b0f24a4e85e41dd4741b2`

Focus similarity review result modes

- Make Similarity Review queue cards act as focused view selectors
- Show either row-level warnings or duplicate clusters, not both at once
- Add pagination for duplicate clusters
- Keep shared taxonomy filters applied across review modes

## 2026-06-01 - `796a0bb`

**Author:** Spiros Kontopoulos

**Full commit:** `796a0bb23e7313171fc78a54418ad5d5480460d3`

Add similarity review duplicate clusters

- Add grouped duplicate cluster data to Similarity Review
- Show cluster summaries and expandable member drafts
- Link cluster members back to generation batch references
- Prepare Similarity Review for focused cluster/table modes

## 2026-06-01 - `08a5d78`

**Author:** Spiros Kontopoulos

**Full commit:** `08a5d7899572ceac68a900f2362a64bfebe447ab`

Add similarity review duplicate rate summary

- Add duplicate-case metrics for the current filter scope
- Count each affected draft as one duplicate case
- Show duplicate rate, total drafts, and warning-message totals
- Keep warning messages as secondary detail for review

## 2026-06-01 - `d2f7df9`

**Author:** Spiros Kontopoulos

**Full commit:** `d2f7df951070b1ceb6ab6417c56a5b36e3449542`

Polish similarity review filters

- Reuse the shared admin taxonomy filter panel on Similarity Review
- Add technology, taxonomy, question type, difficulty, and batch filters
- Extend duplicate-warning review API with taxonomy filters
- Add page-specific Similarity Review styling

## 2026-06-01 - `9729123`

**Author:** Spiros Kontopoulos

**Full commit:** `9729123251d206a61637f4929d4f5a4779b43581`

Link duplicate warning draft references

- Link duplicate warning draft and batch references from validation notes
- Add generated draft row anchors for future deep linking
- Preserve existing validation note display behavior
- Improve admin navigation between duplicate drafts

## 2026-06-01 - `1144d2c`

**Author:** Spiros Kontopoulos

**Full commit:** `1144d2c224a62da1288cf91a36da8774d5146338`

Add cross-batch duplicate warnings

- Compare new AI drafts against approved questions and older drafts
- Store non-blocking duplicate warnings in existing validation errors
- Add fallback matching for older drafts without pattern metadata
- Include batch and draft references in duplicate warning messages

## 2026-06-01 - `8a64355`

**Author:** Spiros Kontopoulos

**Full commit:** `8a64355feadbadc0358720a58bb845a407a2958d`

Store question similarity pattern metadata

- Add compact pattern metadata for AI drafts and approved questions
- Store pattern summary, pattern key, target key, and metadata JSON
- Add pattern service and self-check coverage
- Prepare similarity data for cross-batch duplicate warnings

## 2026-06-01 - `2f20843`

**Author:** Spiros Kontopoulos

**Full commit:** `2f2084347e7d3b4e999dd982da5ba702e7a92012`

Harden question similarity signatures

- Improve deterministic normalization for text, code, and answers
- Make answer signatures independent of option order
- Add signature self-check coverage for normalization behavior
- Bump fingerprint version to question_similarity.v1.1

## 2026-06-01 - `f5f2d83`

**Author:** Spiros Kontopoulos

**Full commit:** `f5f2d836e75278c540663b49ec3965e8ca284789`

Add question similarity fingerprint foundation

- Add question_similarity subsystem for deterministic signatures
- Store prompt, code, answer, and full-question fingerprints
- Populate signatures for AI drafts and approved questions
- Centralize duplicate warning helpers for future similarity work

## 2026-05-31 - `3163712`

**Author:** Spiros Kontopoulos

**Full commit:** `3163712727201c99237ca4cee64b74b9ddd3615b`

Harden AI execution cost rollups

- Roll up plan-item and batch usage directly from execution jobs
- Treat retries and failed attempts with usage as billable accounting records
- Add execution usage summary to the AI generation detail page
- Clarify all-attempt cost semantics in the admin UI
- Keep draft rows focused on review content

## 2026-05-31 - `555a39d`

**Author:** Spiros Kontopoulos

**Full commit:** `555a39d26f4feded4e495083e977f0d14e759b0f`

Add execution job retry tracking

- Add retry and error-category metadata to AI execution jobs
- Scope attempt numbering per normal-API chunk
- Add endpoint for retrying one failed execution chunk
- Refresh batch and plan-item status after retry attempts
- Show retry metadata and retry action in the detail UI

## 2026-05-31 - `3039e6a`

**Author:** Spiros Kontopoulos

**Full commit:** `3039e6a250c202f1db2c6bdc59ffeeae0b16a512`

Add normal API chunking for AI generation

- Split large normal-API plan items into chunks capped at 10 questions
- Create one execution job per provider request chunk
- Add chunk metadata to execution jobs and API responses
- Aggregate chunk results back onto plan items and batches
- Show chunk details in the AI generation detail execution jobs UI

## 2026-05-31 - `4087ac4`

**Author:** Spiros Kontopoulos

**Full commit:** `4087ac4c689c8dfa444079d12f1138e3dbedf667`

Show AI generation execution jobs in detail UI

- Add execution jobs section to AI generation batch detail
- Show provider, model, status, requested/generated counts, tokens, cost, and timestamps
- Add latest execution metadata to plan item rows
- Keep draft question rows focused on review content
- Add responsive styling and patch notes

## 2026-05-31 - `c63ca14`

**Author:** Spiros Kontopoulos

**Full commit:** `c63ca14d017d9d4658768d2702225ebe6776fa4b`

Add AI generation execution job foundation

- Add execution job table linked to AI generation batches and plan items
- Record one execution job per provider attempt during batch runs
- Expose execution jobs in batch and plan item detail responses
- Keep existing batch and plan-item execution metadata mirrored
- Update AI Generation Create live estimate for Blueprint-loaded previews

## 2026-05-31 - `483fb23`

**Author:** Spiros Kontopoulos

**Full commit:** `483fb23c5a6da6cca6429742bcfd0bbf22412873`

Polish Blueprint candidate loading safety

- Align Blueprint candidate UI limits with backend limits
- Skip duplicate Blueprint cells when appending candidates
- Refresh Blueprint priority metadata after editing preview rows
- Allow manual count overrides while showing Blueprint gap warnings
- Remove confusing request estimate wording

## 2026-05-31 - `1f160d6`

**Author:** Spiros Kontopoulos

**Full commit:** `1f160d6e7987655be620ac013b5555d413086139`

Polish Blueprint candidate controls in generation create

- Add Replace and Append modes for Blueprint candidate loading
- Show candidate request estimate before loading
- Merge duplicate exact targets when appending candidates
- Add clearer Blueprint loading and empty states
- Preserve manual create-batch confirmation behavior

## 2026-05-30 - `a6c9543`

**Author:** Spiros Kontopoulos

**Full commit:** `a6c9543297fd0d9f86af71d78f99ad97e8d53b32`

Show Blueprint priority in AI plan preview

- Preserve Blueprint priority metadata for candidate-loaded plan rows
- Enrich exact manual preview rows using Blueprint coverage lookup
- Add Blueprint priority column to the AI Generation Create preview table
- Clear stale priority metadata when preview row difficulty changes
- Keep backend behavior unchanged by reusing the existing coverage endpoint

## 2026-05-30 - `20a60fb`

**Author:** Spiros Kontopoulos

**Full commit:** `20a60fb2c833a49d1803d43a35ac4057ab51e0a5`

Add Blueprint candidate flow to AI generation create

- Add Blueprint assist section to the AI Generation Create page
- Load ranked Blueprint candidates as editable manual plan rows
- Allow Blueprint-sourced plans to create batches from explicit plan_items
- Preserve the existing staged builder preview and create flow
- Add styling and patch notes for the Blueprint candidate assist UI

## 2026-05-30 - `b4dfdd4`

**Author:** Spiros Kontopoulos

**Full commit:** `b4dfdd4d6c7f6f56064dbb3f60a3c4a91276a56b`

Add blueprint generation candidate bridge

- Add read-only Blueprint generation candidate service
- Expose ranked planner-ready candidates from recommended Blueprint gaps
- Return manual plan-item payloads without creating AI generation batches
- Add top generation candidates section to the Blueprint admin page
- Keep Blueprint coverage and AI generation execution behavior unchanged

## 2026-05-30 - `745a9c2`

**Author:** Spiros Kontopoulos

**Full commit:** `745a9c267dddb8a876f2fbfd0355a9c511f21621`

Extract AI generation planner into subsystem

- Add ai_generation subsystem package for generation business logic
- Move planner service into app/ai_generation/planner_service.py
- Update AI generation router imports to use the subsystem path
- Keep a compatibility wrapper for older planner imports
- Preserve existing API behavior during the refactor

## 2026-05-30 - `854b3c9`

**Author:** Spiros Kontopoulos

**Full commit:** `854b3c9857abbe414b643b971b45eac606ee6c36`

Add blueprint generation priority scoring

- Add Blueprint priority scoring service inside the subsystem package
- Expose generation priority score, bucket, and reasons in coverage rows
- Sort Blueprint coverage by generation priority by default
- Add sortable Priority column to the admin Blueprint page
- Keep covered and non-automatic cells out of generation priority ranking

## 2026-05-30 - `b4a7be1`

**Author:** Spiros Kontopoulos

**Full commit:** `b4a7be1c4956ba88e878b57d7d5eed824065d965`

Polish blueprint suitability coverage display

- Clarify targetless Blueprint rows in the admin coverage table
- Avoid showing manual-only cells as covered target rows
- Reword coverage filters around automatic target coverage
- Add small styling for no-target and policy-note row details

## 2026-05-30 - `67c1fb4`

**Author:** Spiros Kontopoulos

**Full commit:** `67c1fb47accd5446b19ec7582141b70411ecb15c`

Add suitability-aware blueprint coverage tiers

- Resolve suitability tiers inside Blueprint coverage cells
- Target only strong and secondary fit combinations automatically
- Keep weak and unrated cells visible without inflating gaps
- Replace Blueprint difficulty queues with suitability work queues
- Add suitability badges and target-mode details to the admin table

## 2026-05-30 - `d429500`

**Author:** Spiros Kontopoulos

**Full commit:** `d429500f6f271a3c87e0e4647d02afbfb2f5dae8`

Add blueprint coverage filters

- Add taxonomy, question type, difficulty, coverage, and search filters to Blueprint coverage
- Support server-side filtering and ordering for accurate pagination
- Reuse the shared admin question filter panel pattern
- Add result count feedback and polish filter width handling

## 2026-05-30 - `b5ad2f5`

**Author:** Spiros Kontopoulos

**Full commit:** `b5ad2f505419f878506221d2af82e8de85dc48ad`

Add blueprint coverage admin page

- Add Admin Blueprint page backed by the coverage/gap endpoint
- Show blueprint summary cards for cells, targets, approved, pending, and gaps
- Add queue-card filters for hard gaps, all cells, and difficulty-specific gaps
- Add paginated focused coverage rows table

## 2026-05-30 - `6b3f02b`

**Author:** Spiros Kontopoulos

**Full commit:** `6b3f02b4985a64223ad367f0e69242120e7b5722`

Add blueprint coverage gap endpoint

- Add live blueprint coverage calculation endpoint
- Expand active blueprint rules across concepts, eligible question types, and difficulties
- Count approved questions and pending AI drafts separately
- Return summary totals and paginated coverage/gap rows

## 2026-05-30 - `9d74a83`

**Author:** Spiros Kontopoulos

**Full commit:** `9d74a83308702cb3054822cd0cdccd2a818c5b3f`

Create blueprint backend subsystem

- Add internal blueprint package for rule services and validation
- Move blueprint rule CRUD logic out of the router
- Keep blueprint rule routes as a thin HTTP layer
- Preserve existing blueprint rule API behavior

## 2026-05-30 - `c3b0daa`

**Author:** Spiros Kontopoulos

**Full commit:** `c3b0daa14356744aa53f91dcc771eaa3c34404ab`

Add blueprint rules admin page

- Add frontend API client for blueprint rule CRUD endpoints
- Add admin page for listing, creating, editing, and toggling blueprint rules
- Support taxonomy-scoped rules from global through concept
- Add Question Bank navigation entry for Blueprint Rules

## 2026-05-30 - `d40b379`

**Author:** Spiros Kontopoulos

**Full commit:** `d40b379995186088e8654f789d8075caa36ceae5`

Add blueprint rule admin API

- Add admin CRUD endpoints for blueprint rules
- Validate taxonomy scope targets, question types, and difficulty values
- Support deactivate and reactivate workflows
- Prevent duplicate active blueprint rules for the same scope and selector

## 2026-05-30 - `b6c0951`

**Author:** Spiros Kontopoulos

**Full commit:** `b6c09516df47630fc2852a87d23086eafc12b91e`

Add blueprint rule model

- Add blueprint_rules table for rule-based question bank targets
- Support taxonomy scopes from global through concept
- Add optional question type, difficulty, target count, priority, source, notes, and active flag
- Add Pydantic schemas for blueprint rule create, update, read, and list flows

## 2026-05-30 - `134e4ef`

**Author:** Spiros Kontopoulos

**Full commit:** `134e4ef3f53b2b851c5143aab0db01b767b8f330`

Add suitability review queues

- Add backend suitability review queues for direct, inherited, missing, and AI-draft coverage
- Add summary counts and paginated queue data to taxonomy audit diagnostics
- Add Taxonomy Audit UI cards and table for suitability review queues
- Reuse active taxonomy audit scope filters for suitability review

## 2026-05-30 - `ce28f44`

**Author:** Spiros Kontopoulos

**Full commit:** `ce28f44c83bf1596f523246f609f7b61677e2ff4`

Add suitability review queue backend

- Add taxonomy audit endpoint for suitability review queues
- Return summary counts for direct, inherited, missing, and AI-draft suitability coverage
- Add paginated concept queues with full taxonomy paths and review metadata
- Add frontend API helper for the future suitability review UI

## 2026-05-30 - `39c4f54`

**Author:** Spiros Kontopoulos

**Full commit:** `39c4f543ef4c01621ebc8816e5fdecf911e20a75`

Apply AI suitability suggestions to new concepts

- Convert staged AI suitability suggestions into direct concept suitability rules
- Apply suggestions during the explicit create-concept-and-apply workflow
- Skip invalid, ineligible, duplicate, or already-existing suitability rules
- Make mock new-concept suggestions unique so repeated tests do not collide

## 2026-05-30 - `60647d9`

**Author:** Spiros Kontopoulos

**Full commit:** `60647d9e4cd389f6709fe4b4d52c88fc76917fc5`

Stage AI suitability suggestions for new concepts

- Extend AI classification output to include suggested suitability rules
- Store suggested suitability rules as staged JSON on generated drafts
- Display staged suitability suggestions in the AI generation detail review panel
- Add migration and Alembic merge revision for the new staging field

## 2026-05-30 - `f3c7f25`

**Author:** Spiros Kontopoulos

**Full commit:** `f3c7f255f84678da76d52f6d99046ddad44165f0`

Add multi-target suitability selector pages

- Add target-aware Step 5 pages for module, topic, subtopic, and concept selections
- Resolve suitability recommendations for the active target page
- Store question-type selections separately per target page
- Keep page-level apply, select, and clear actions scoped to the active target
- Preserve target-specific question-type payloads for preview and generation

## 2026-05-30 - `1bc5164`

**Author:** Spiros Kontopoulos

**Full commit:** `1bc5164b5245ec7c6b2990d1bbcf09bef332ba37`

Polish AI generation detail display

- Include subtopic names in plan item and draft target paths
- Remove repeated provider/model column from generated draft rows
- Keep batch-level model metadata visible in the generation summary

## 2026-05-30 - `1371b79`

**Author:** Spiros Kontopoulos

**Full commit:** `1371b79e789e160412910f9c2228ec9d7cb0ba40`

Warn about difficulty mismatch in generation create

- Add amber warnings when selected difficulty may not match the focused suitability target
- Surface the warning near both the suitability selector and difficulty selection summary
- Keep generation allowed while making possible concept drift visible to admins

## 2026-05-30 - `203a87e`

**Author:** Spiros Kontopoulos

**Full commit:** `203a87e0994d867faf8271244d06adf02212f507`

Add suitability-aware question type selector

- Redesign Generation Create Step 5 around suitability-aware question-type rows
- Show suitability scores and compact source labels directly inside the selector
- Move long suitability notes into hover tooltips
- Remove automatic default question-type selection so admins choose explicitly
- Highlight the active difficulty weighting used for recommendation scores

## 2026-05-30 - `4366377`

**Author:** Spiros Kontopoulos

**Full commit:** `43663773c283d5499ccf3a3c4cc6ab4cb2aa1dbc`

Add suitability-aware question type selector

- Redesign Generation Create Step 5 around question-type rows with suitability context
- Show suitability score and source directly inside the selector table
- Move long suitability notes into hover tooltips to keep the table compact
- Preserve manual selection and apply-recommendations behavior

## 2026-05-29 - `bca13fa`

**Author:** Spiros Kontopoulos

**Full commit:** `bca13fa3d7179cca10e316089c7abf7bfa3ed593`

Show suitability recommendations in generation create

- Add question-type suitability recommendations to the generation create workflow
- Resolve direct and inherited suitability rules for selected taxonomy targets
- Show effective scores, source rules, difficulty weights, and recommendation notes
- Allow admins to apply top recommendations while keeping manual selection available

## 2026-05-29 - `7d58598`

**Author:** Spiros Kontopoulos

**Full commit:** `7d58598fcac33394b437c1706be3b16a10dd672b`

Add suitability inheritance resolver

- Add resolver endpoint for ranking question-type suitability by taxonomy scope
- Support concept, subtopic, topic, and module inheritance when resolving rules
- Apply optional difficulty weights to calculate effective recommendation scores
- Add admin preview UI for testing direct and inherited suitability recommendations

## 2026-05-29 - `6f7899a`

**Author:** Spiros Kontopoulos

**Full commit:** `6f7899a90f30a11d83e1f930d388b83214a094ad`

Add suitability rule management

- Add create, edit, deactivate, and reactivate actions for question-type suitability rules
- Add duplicate protection for taxonomy target and question type combinations
- Add admin form workflow for managing suitability scores and difficulty weights
- Keep seeded rules editable while preserving soft-deactivation behavior

## 2026-05-29 - `b909cf0`

**Author:** Spiros Kontopoulos

**Full commit:** `b909cf0d12afaf9da3129c209572548be1abfd37`

Add question type suitability foundation

- Add question-type suitability rule model, schema, migration, and read API
- Seed the initial Python Lists suitability draft into database-backed rules
- Add read-only admin page for browsing suitability by taxonomy target and question type
- Add filtering, summary cards, and shared pagination for suitability rules

## 2026-05-29 - `9ecdba0`

**Author:** Spiros Kontopoulos

**Full commit:** `9ecdba0f4d75399c1ce0fb87f3ff273b61c50f49`

Add server pagination for taxonomy audit diagnostics

- Add backend pagination parameters for active taxonomy audit diagnostic queues
- Return queue metadata and total counts for paginated audit sections
- Load only the selected diagnostic queue page from the frontend
- Keep shared admin pagination aligned with audit queue cards

## 2026-05-29 - `6759bf4`

**Author:** Spiros Kontopoulos

**Full commit:** `6759bf48cdcd7326cc707c956f6b4f85a057b8fa`

Standardize admin queue table styling

- Reuse shared admin table wrappers for newer queue/workbench tables
- Align AI draft inbox and concept enrichment tables with existing admin UI patterns
- Improve table headings, spacing, borders, and action-column consistency
- Keep queue pages visually consistent after recent admin UI additions

## 2026-05-29 - `2ff5049`

**Author:** Spiros Kontopoulos

**Full commit:** `2ff504959d6b5fa84681273c6d3750c5d41e6908`

Add global AI draft review inbox

- Add all-batch AI draft review inbox under the AI Generation admin section
- Add backend draft review filters, queue counts, and paginated results
- Add queue cards for needs-review, new-concept, failed, duplicate, and ready drafts
- Link draft rows back to their source generation batches
- Summarize validation notes to keep inbox rows readable

## 2026-05-29 - `9b1da4a`

**Author:** Spiros Kontopoulos

**Full commit:** `9b1da4a063190571aa2ecd2cde8ef3b2c6da09db`

Add taxonomy filters to concept enrichment

- Add backend taxonomy-scope filters for concept enrichment queues
- Add cascading field, technology, domain, module, topic, and subtopic filters
- Keep queue counts and paginated rows aligned with the selected taxonomy scope
- Reset pagination when enrichment filters change

## 2026-05-29 - `028f7c0`

**Author:** Spiros Kontopoulos

**Full commit:** `028f7c0a509fea404d572eeeb8d2a383b7fbaff2`

Add reject action for AI-suggested concepts

- Add backend action to reject unresolved AI new-concept suggestions
- Add Concept Enrichment reject button with confirmation flow
- Remove rejected suggestions from the AI-suggested concepts queue
- Keep rejected drafts blocked from approval until reviewed through another workflow

## 2026-05-29 - `2a125b5`

**Author:** Spiros Kontopoulos

**Full commit:** `2a125b54de06ecedd18062f15b0edcf5af661050`

Add accordion admin navigation

- Group admin sidebar links into collapsible navigation sections
- Automatically open the active section based on the current route
- Keep dashboard and public-site links as top-level navigation items
- Move admin navigation styles into a dedicated CSS file

## 2026-05-29 - `8770ad0`

**Author:** Spiros Kontopoulos

**Full commit:** `8770ad052743f120c1dccefcd9adf4580d76c3c0`

Split shared admin CSS foundation

- Split large admin stylesheet into focused shared admin CSS files
- Keep admin.css as the central import entrypoint for existing page imports
- Move Test Lab page-specific styles into a dedicated page stylesheet
- Preserve existing CSS order to reduce visual regression risk

## 2026-05-29 - `05baed9`

**Author:** Spiros Kontopoulos

**Full commit:** `05baed93c20208626ec73c989bc2645524f4a149`

Add admin test lab for AI generation cases

- Add Admin Test Lab page for creating mock AI generation review cases
- Add backend endpoint for generating classification test batches
- Support passed, missing, invalid ID, low-confidence, and new-concept cases
- Wire Test Lab into admin routing and navigation for repeatable workflow testing

## 2026-05-29 - `3929a4f`

**Author:** Spiros Kontopoulos

**Full commit:** `3929a4f89333d680bfdaa3cf2c9b919327e620be`

Add AI-suggested concept actions to enrichment queue

- Add create-and-apply action for unresolved AI-suggested concepts
- Add existing-concept selection flow inside the concept enrichment queue
- Reuse AI generation review endpoints for concept resolution actions
- Refresh the active queue after successful concept resolution

## 2026-05-29 - `86a13c2`

**Author:** Spiros Kontopoulos

**Full commit:** `86a13c22657cc6574137286524c6b24c93f307c9`

Add server pagination for concept enrichment queues

- Add backend queue, page, and page-size parameters for concept enrichment data
- Load only the selected concept work queue instead of slicing large lists in the frontend
- Keep summary and queue counts while paginating active queue rows from the API
- Reset pagination when filters, queue selection, or page size changes

## 2026-05-29 - `95e9924`

**Author:** Spiros Kontopoulos

**Full commit:** `95e99245700078ff14ddb26e1ea2b174391cc547`

Organize taxonomy audit into diagnostic queues

- Replace always-open audit sections with clickable diagnostic queue cards
- Show one focused audit table at a time with shared admin pagination
- Improve audit page readability for large concept coverage lists
- Keep summary cards visible while making detailed diagnostics easier to scan

## 2026-05-29 - `533b544`

**Author:** Spiros Kontopoulos

**Full commit:** `533b544477c5b39bf75da939c8100a97078c2aa1`

Organize concept enrichment into work queues

- Add clickable concept work-queue cards for enrichment workflows
- Show one focused queue table at a time instead of all sections open by default
- Add subtopics-without-concepts queue and shared pagination support
- Improve concept enrichment labels and page organization for admin review

## 2026-05-29 - `f126f7c`

**Author:** Spiros Kontopoulos

**Full commit:** `f126f7cf6a6c724218bbd53a7fb8c7083b2b35a7`

Add concept enrichment admin foundation

- Add backend concept enrichment endpoint with summary and concept inventory data
- Add admin Concept Enrichment page with filters, AI suggestion queue, and inventory table
- Add shared admin pagination for concept inventory with 10/25/50 row options
- Wire the new page into admin routing and taxonomy navigation

## 2026-05-29 - `83021b3`

**Author:** Spiros Kontopoulos

**Full commit:** `83021b3cdd344f88bf0865ac196f761925920a46`

Add existing concept review action for AI drafts

- Add backend endpoints for loading and applying existing concepts
- Allow admins to resolve suggested-new-concept drafts without creating duplicates
- Add frontend API helpers and inline concept selection UI
- Keep the generated draft preview updated after applying a concept

## 2026-05-29 - `d0f1daf`

**Author:** Spiros Kontopoulos

**Full commit:** `d0f1daff35f518a1b869dd3ea91b37c8b2156a57`

Add suggested concept creation from AI drafts

- Adds a review action for creating AI-suggested concepts from generated drafts
- Applies created or reused concepts back to the staged draft classification
- Updates the draft UI in place after concept creation
- Clarifies suggested-new-concept display in the classification review panel

## 2026-05-29 - `7596727`

**Author:** Spiros Kontopoulos

**Full commit:** `7596727aa84ec208c2e0e4b86401d197213ee66b`

Improve classification review workflow

- Adds a dedicated Classification column for generated draft review
- Blocks unsafe reverse-classified drafts from manual and bulk approval
- Adds clearer classification review states for passed, failed, mismatch, and needs-review drafts
- Improves accept-suggestion UX so reviewed drafts update in place

## 2026-05-29 - `8056e1a`

**Author:** Spiros Kontopoulos

**Full commit:** `8056e1a44e4642df7b0dd54324723838ad8cc6c3`

Add mock classification failure cases

- Adds mock reverse-classification cases for missing, invalid, low-confidence, and new-concept outputs
- Supports safer testing of failed and review-required classification states
- Improves generated draft classification badge handling for failure scenarios
- Prepares reverse-generation approval guards for unsafe classification results

## 2026-05-29 - `00bd4c0`

**Author:** Spiros Kontopoulos

**Full commit:** `00bd4c080c9ff0cadcf27cffd6afc8dc86a54f5c`

Show generation mode and classification status badges

- Shows normal and reverse generation mode badges in AI batch list and detail views
- Renames provider execution display to clarify it means provider API mode
- Adds compact classification status badges under generated draft status
- Highlights reverse drafts with passed, review, missing, or mismatched classification metadata

## 2026-05-29 - `eb72dbd`

**Author:** Spiros Kontopoulos

**Full commit:** `eb72dbd5b45fdf12987320879cc678e7e797643a`

Add admin classification suggestion review

- Adds an admin action for accepting normalized AI classification suggestions
- Shows current draft targets beside AI-suggested taxonomy and question type metadata
- Adds an Accept suggestion flow for pending generated drafts
- Improves reverse-generation review visibility inside the generated question UI

## 2026-05-28 - `af2fddb`

**Author:** Spiros Kontopoulos

**Full commit:** `af2fddb588694459ff8f053f4bfda3f1990c3a2e`

Normalize reverse generation classification suggestions

- Validates AI-returned subtopic, concept, question type, and difficulty suggestions against the DB
- Stores only normalized classification metadata on generated AI drafts
- Marks uncertain or conflicting classification results for taxonomy review
- Allows reverse-mode mock execution now that classification normalization is guarded

## 2026-05-28 - `1ca1291`

**Author:** Spiros Kontopoulos

**Full commit:** `1ca1291564980634cb5d35237126809083cde9e3`

Send taxonomy slices to question service

- Builds compact local taxonomy slices for generation plan items
- Sends scoped subtopics, concepts, and question types to question-service
- Updates question-service prompts to classify reverse output using the supplied slice
- Keeps normal generation output backward-compatible without classification metadata

## 2026-05-28 - `9754047`

**Author:** Spiros Kontopoulos

**Full commit:** `9754047f94b38534557a8018ee7c95bb7a711e30`

Add question-service classification output contract

- Adds reverse-generation classification metadata to the question-service response contract
- Extends prompt rules for normal and reverse generation modes
- Maps classification fields from question-service responses into quiz-api draft schemas
- Keeps reverse execution guarded until taxonomy normalization and review workflows are added

## 2026-05-28 - `1115703`

**Author:** Spiros Kontopoulos

**Full commit:** `1115703b85f76333e5f529e0eb67637168780465`

Add AI draft classification metadata

- Adds database fields for reverse-generation taxonomy and question-type suggestions
- Exposes suggested subtopic, concept, question type, difficulty, confidence, and review flags in AI draft schemas
- Shows AI classification suggestions in the generated draft review UI
- Prepares reverse generation drafts for normalization and admin review workflows

## 2026-05-28 - `52b6b4a`

**Author:** Spiros Kontopoulos

**Full commit:** `52b6b4a598bc6a872293614ce3284a1eba6a90a0`

Add reverse generation mode contract

- Adds normal and reverse generation mode support to the AI generation contract
- Allows reverse mode to preview and create broader taxonomy-scoped generation plans
- Keeps normal mode behavior compatible with the existing exact-target workflow
- Blocks reverse-mode execution until AI classification metadata is added

## 2026-05-28 - `f506dd9`

**Author:** Spiros Kontopoulos

**Full commit:** `f506dd99faeba5fa2b8705c6e84f63506067c828`

Enrich Core Language taxonomy concepts

- Expands Strings, Dictionaries, Sets, Tuples, and Control Flow with behavior-based concepts
- Maps enriched concepts to active subtopics across the Core Language taxonomy
- Cleans up superseded empty subtopics from earlier taxonomy versions
- Completes the Core Language enrichment pass after Lists and Functions

## 2026-05-28 - `3e26e5e`

**Author:** Spiros Kontopoulos

**Full commit:** `3e26e5ee8ef11f44147f3f9d6ee5a45bf73522b0`

Enrich Python Functions taxonomy concepts

- Expands Functions into a richer behavior-based taxonomy area
- Adds coverage for calls, returns, arguments, scope, closures, recursion, decorators, and lambdas
- Maps all new Function concepts to active subtopics
- Prepares Functions as the second Core Language enrichment pilot after Lists

## 2026-05-28 - `2c09ea1`

**Author:** Spiros Kontopoulos

**Full commit:** `2c09ea1bf89f1523c6c5fc56d6e2105c0596e3d0`

Add Lists question type suitability draft

- Adds concept-level question type suitability scores for the Lists pilot
- Defines reusable suitability profiles for indexing, slicing, mutation, copying, nesting, and sorting concepts
- Adds beginner, intermediate, and advanced difficulty weights for future blueprint planning
- Keeps the suitability draft separate from runtime seeding until the blueprint model is added

## 2026-05-28 - `77674a8`

**Author:** Spiros Kontopoulos

**Full commit:** `77674a87e01ec09b59ab2254168dc6383ba215b3`

Enrich Python Lists taxonomy concepts

- Expands Lists into a richer behavior-based concept pilot
- Adds Length, Membership & Iteration as a Lists subtopic
- Maps new concepts across creation, access, slicing, methods, copying, nested lists, and sorting
- Prepares Lists as the first blueprint and fingerprint pilot area

## 2026-05-28 - `3e4ffdd`

**Author:** Spiros Kontopoulos

**Full commit:** `3e4ffdd5e4ce6a6448cfb191fc1d19ccb01b5916`

Make taxonomy coverage audit scope-aware

- Adds backend scope filtering for field, technology, domain, module, and topic audits
- Returns selected audit scope metadata with coverage results
- Adds a polished cascading audit scope selector in the admin UI
- Defaults the audit page to Python and keeps JSON export tied to the selected scope

## 2026-05-28 - `3a5a652`

**Author:** Spiros Kontopoulos

**Full commit:** `3a5a65204ffc736884bb91474e05d5802ed1d050`

Add admin taxonomy coverage audit page

- Adds a frontend API client for the taxonomy audit coverage endpoint
- Replaces the audit placeholder with a real admin Coverage Audit page
- Shows summary cards, detailed gap sections, missing metadata, and coverage breakdowns
- Adds JSON export support for audit review and future planning

## 2026-05-28 - `746a4df`

**Author:** Spiros Kontopoulos

**Full commit:** `746a4df79f44dfff0a199254c21c5b492af65429`

Add taxonomy coverage audit endpoint

- Adds a read-only admin taxonomy audit coverage endpoint
- Reports empty taxonomy areas, concept coverage gaps, and missing question metadata
- Includes approved and pending review question coverage summaries
- Prepares the backend foundation for the admin Coverage Audit page

## 2026-05-28 - `790bc6d`

**Author:** Spiros Kontopoulos

**Full commit:** `790bc6d9de1875d53ddb2d4fe2f25b97bf252e1f`

Organize admin navigation into grouped sections

- Groups admin navigation into Taxonomy, Question Bank, AI Generation, and Quiz Management
- Renames the current taxonomy page under Manage Taxonomy
- Adds future backend-quality routes as coming-soon admin pages
- Keeps question type suitability connected to the existing taxonomy mapping page

## 2026-05-28 - `ab9dd35`

**Author:** Spiros Kontopoulos

**Full commit:** `ab9dd35f89164a0d188367fc3006c36ed97e76ed`

Remove dashes from text in homepage

## 2026-05-28 - `c54fc6e`

**Author:** Spiros Kontopoulos

**Full commit:** `c54fc6efde5da1c25404098c1ec22420f7069cad`

Refine homepage hero technology tree

- Replaces the hero path-tree image with a styled HTML technology tree
- Adds the missing Core Language taxonomy step between Python and Data Structures
- Removes the topic-based practice note from the floating tree card
- Updates hero copy to use technologies, domains, topics, and concepts wording

## 2026-05-28 - `c60c9be`

**Author:** Spiros Kontopoulos

**Full commit:** `c60c9be1ab2038dba03ffc7f7d67d705c7fe8558`

Polish homepage hero and navbar styling

- Refines hero badges with softer product-aligned colors
- Improves the technology path floating card readability and placement
- Adjusts concept feedback card positioning in the hero visual stack
- Adds subtle Codiquiz-branded styling to the public navbar and auth actions

## 2026-05-27 - `4ae01e5`

**Author:** Spiros Kontopoulos

**Full commit:** `4ae01e57cecd2d290b54737ec0f8a8b88dcd6958`

Make homepage summary data DB-driven

- Adds a public homepage summary endpoint for stats and field data
- Loads homepage question, quiz, domain, and concept coverage stats from the backend
- Renders Browse by field from DB taxonomy fields with frontend icon mapping
- Refines homepage hero labels and replaces the footer quality logo with a gold quality badge

## 2026-05-27 - `db2c5bf`

**Author:** Spiros Kontopoulos

**Full commit:** `db2c5bfb742bb41e83ed8ba04c33e4d90d2a9918`

Fix homepage carousel click and drag behavior

- Restores normal technology card clicks after drag handling changes
- Keeps edge technology cards clickable for one-step carousel movement
- Prevents click events from being swallowed after non-drag interactions
- Removes edge opacity blinking by only enabling drag state after real movement

## 2026-05-27 - `967b0ff`

**Author:** Spiros Kontopoulos

**Full commit:** `967b0fff3ebe21d04fadfb113952ef4182697f58`

Finalize homepage technology carousel interactions

- Refines auto-slide timing and idle resume behavior
- Adds arrow click, arrow hover, drag, and edge-card click interactions
- Restores edge-card click-to-slide while removing hover-to-slide behavior
- Adjusts side technology opacity for clearer carousel edge states

## 2026-05-27 - `03c0177`

**Author:** Spiros Kontopoulos

**Full commit:** `03c0177c9a699df3ccd8982fc9a3db0444d7180f`

Refine homepage technology carousel interactions

- Improves the technology carousel with looping slide behavior
- Adds drag support and side-card interaction behavior
- Adjusts carousel timing, arrow hover behavior, and edge-card opacity
- Keeps the Start by Technology section interactive while preserving the public homepage layout

## 2026-05-27 - `8b55b34`

**Author:** Spiros Kontopoulos

**Full commit:** `8b55b340b0d9125a4080ee3c80e2b16c26add319`

Add homepage technology carousel

- Converts the Start by Technology section into a horizontal carousel
- Adds auto-sliding, arrow navigation, and drag interaction support
- Extends the static coming-soon technology list with Java, Ruby, and Elixir
- Refines carousel layout after removing the reset-to-Python behavior

## 2026-05-27 - `4266a08`

**Author:** Spiros Kontopoulos

**Full commit:** `4266a08ba1a9d83bc4e6ebba4b082bc11f071670`

Merge homepage info cards into hero

- Removes the separate homepage info-card bar below the hero
- Merges topic-based practice into the technology path hero card
- Adds the growing question bank badge next to the topic-based question bank label
- Refines the hero code example with option C as the correct answer state

## 2026-05-27 - `f90dfbf`

**Author:** Spiros Kontopoulos

**Full commit:** `f90dfbf0e8494f269906b9d3f3c65a5e895fe82c`

Refine homepage layout and public footer

- Moves homepage info cards below the hero and above the stats strip
- Refines hero visual cards, answer state, and heading colors
- Improves footer logo rendering on dark backgrounds
- Centers the public header content within the page layout rail

## 2026-05-27 - `5c0acdd`

**Author:** Spiros Kontopoulos

**Full commit:** `5c0acdd16d1290dfa13ecd06af89cbf0747d8e3e`

Refine public homepage logo and info cards

- Uses the final Codiquiz SVG logo and label assets in the public UI
- Keeps the improved homepage info-card icons and visual styling
- Updates homepage hero, footer, and supporting public layout styles
- Preserves the current working visual baseline before repositioning homepage info cards

## 2026-05-27 - `8039022`

**Author:** Spiros Kontopoulos

**Full commit:** `8039022d6b7df8bfaa6c2d052d430db0802e07ae`

Polish public homepage and technology icons

- Adds reusable public technology icon rendering and Devicon support
- Wires technology logos into the Python technology page and homepage cards
- Reworks the public homepage hero, stats, practice cards, and how-it-works section
- Adds the dark quality/footer section and reusable Codiquiz logo component
- Updates the admin AI generation smoke test to avoid brittle mock snippet assumptions

## 2026-05-27 - `3f8deed`

**Author:** Spiros Kontopoulos

**Full commit:** `3f8deed9cdda848f88bedbee3d0d96b4ba642398`

Add public technology icon layer

- Adds Devicon support and a reusable public TechnologyIcon component
- Wires technology logos into the public Python technology page
- Uses the real Python SVG logo and a neutral SQL fallback icon
- Updates the admin AI generation smoke test to avoid brittle mock snippet assumptions

## 2026-05-27 - `ca2eb0f`

**Author:** Spiros Kontopoulos

**Full commit:** `ca2eb0fb6b4b27dd1ef560a40dff213b9f3d139d`

Extract reusable admin question filter panel

- Adds a reusable admin question filter panel with taxonomy-aware filters
- Shares Apply, Reset, Auto search, and hover dropdown behavior across question pages
- Refactors admin questions to use the shared filter panel
- Adds the same question-bank filter workflow to quiz question management

## 2026-05-26 - `ec8156c`

**Author:** Spiros Kontopoulos

**Full commit:** `ec8156c0da80595e61ffd8e494453af6eda90011`

Improve admin questions filter workflow

- Adds draft/applied filter state so filters do not reload results immediately
- Adds Apply filters, Reset filters, and Auto search behavior
- Adds hover-open filter dropdowns with click/focus fallback
- Fixes dropdown hover usability by removing the trigger/menu gap

## 2026-05-26 - `25ecf3e`

**Author:** Spiros Kontopoulos

**Full commit:** `25ecf3eeb283972a0e8816758571f98ed6f34c8a`

Add subtopic filter to admin questions

- Adds subtopic filtering between topic and concept filters
- Supports technology_subtopic_id in question list and search endpoints
- Shows subtopic metadata in question taxonomy paths
- Keeps existing admin question filters compatible

## 2026-05-26 - `ebc7b28`

**Author:** Spiros Kontopoulos

**Full commit:** `ebc7b28f67dff7d5bf94df5a2fb44b635bec578f`

Make question service subtopic-aware

- Accepts technology subtopic metadata in question generation requests
- Adds subtopic context to mock and OpenAI generation prompts
- Updates prompt rules around Technology -> Domain -> Module -> Topic -> Subtopic -> Concept targeting
- Keeps broad module, topic, and concept generation compatible

## 2026-05-26 - `23370e4`

**Author:** Spiros Kontopoulos

**Full commit:** `23370e410b8b760d386aa97bb069c16328f58c85`

Add subtopic targeting to AI generation builder

- Reworks the generation builder flow into Modules/Topics, Subtopics, Concepts, Question Types, Settings, and Preview
- Adds compact nested targeting UI while preserving the existing staged builder experience
- Supports broad module, broad topic, broad subtopic, and explicit concept-level generation targets
- Extends preview/create/run generation handling with technology subtopic target fields
- Updates regression coverage for the subtopic-aware admin generation flow

## 2026-05-26 - `e2bc7c3`

**Author:** Spiros Kontopoulos

**Full commit:** `e2bc7c3566dc5d9dd9cefc77b636e31c3a326727`

Polish public technology sidebar

- Makes the public technology sidebar more compact and readable
- Adds connector-line styling for nested taxonomy levels
- Improves active, hover, and chevron states for the sidebar tree
- Keeps the DB-driven technology navigation behavior unchanged

## 2026-05-26 - `17fdb37`

**Author:** Spiros Kontopoulos

**Full commit:** `17fdb37cefa118b2c20fafec45a44e94681dca25`

Polish public technology page navigation

- Adds nested public taxonomy routes for domain, module, topic, and subtopic pages
- Makes breadcrumb items clickable for shareable taxonomy navigation
- Collapses the sidebar to the selected taxonomy path
- Fixes active sidebar highlighting by matching both entity level and id
- Updates public smoke coverage for nested taxonomy routes

## 2026-05-26 - `f1d327b`

**Author:** Spiros Kontopoulos

**Full commit:** `f1d327b8950969e861ecb6e7fed22778c4c1bc9a`

Make Python technology page DB-driven

- Replaces static Python technology page data with live taxonomy lookup data
- Renders domains, modules, topics, subtopics, and concepts from the backend tree
- Preserves the V3 public technology page layout with sidebar and main detail states
- Updates public-site smoke coverage for DB-backed taxonomy navigation

## 2026-05-26 - `429c878`

**Author:** Spiros Kontopoulos

**Full commit:** `429c8781fe31329834b0dfdb40678f54aed928e2`

Add admin subtopic management

- Adds subtopics to the admin taxonomy management tree
- Supports creating, editing, deactivating, and reactivating subtopics
- Shows concepts under assigned subtopics while preserving direct topic concepts
- Updates the admin taxonomy hierarchy for Field -> Technology -> Domain -> Module -> Topic -> Subtopic -> Concept

## 2026-05-26 - `77db53e`

**Author:** Spiros Kontopoulos

**Full commit:** `77db53ee0348a67987734f65c48c1670426ff604`

Add taxonomy subtopics foundation

- Adds taxonomy subtopics with Alembic migration and nullable concept mapping
- Refactors seed data into a modular seeding package
- Seeds Python subtopics across the current taxonomy
- Extends lookup schemas and API responses for subtopics
- Keeps existing practice, public-site, and admin generation flows passing

## 2026-05-26 - `af7938d`

**Author:** Spiros Kontopoulos

**Full commit:** `af7938dda38da1923d2b72a2a93575cf7fb565a8`

Build public site V3 foundation

- Reworks the homepage around the final V3 public-site direction
- Adds Featured Practice Paths, practice mode cards, and layered hero visuals
- Updates the Python technology page with module, topic, subtopic, and concept states
- Adds public-site smoke coverage for homepage and technology navigation

## 2026-05-26 - `c91da28`

**Author:** Spiros Kontopoulos

**Full commit:** `c91da28493e89dbc7c3416c785ba1871fbf709cf`

Add public site foundation

- Adds first public homepage and Python technology page foundation
- Adds routes for the public technology page
- Introduces public-site styling for homepage and technology layouts
- Adds Playwright smoke coverage for the public site

## 2026-05-25 - `d8ab657`

**Author:** Spiros Kontopoulos

**Full commit:** `d8ab657209c80c8118211e17339b3d4980e48d38`

Add quick practice regression coverage

- Adds Playwright coverage for broad-module and specific-topic practice setup
- Adds stable test hooks for the quick practice staged flow
- Fixes accordion pointer-event stability during smooth transitions
- Auto-opens Domains after technology taxonomy data loads

## 2026-05-25 - `d2e88ef`

**Author:** Spiros Kontopoulos

**Full commit:** `d2e88ef25c49fec5c56fb145fd276a62b19d4e31`

Polish B5 quick practice staged flow

- Adds a compact staged practice setup flow with horizontal progress
- Restores B4-style next-step side rail and target coverage card
- Loads active technologies dynamically and updates the practice title
- Adds Apply/Edit step controls for domains, modules, topics, and settings
- Keeps quick practice focused on technology, domains, modules, topics, and assessment settings

## 2026-05-25 - `7733932`

**Author:** Spiros Kontopoulos

**Full commit:** `7733932e4c4ee0cda1c764a2f8f9a03ccf2464dd`

Make polished UI changes for practise session

## 2026-05-25 - `e38f48a`

**Author:** Spiros Kontopoulos

**Full commit:** `e38f48ae144c2094ae093e64b751d45d282f12ce`

Build B5 quick practice flow

- Reworks public Practice page into a quick Domain -> Modules -> Topics flow
- Adds rich module/topic selection UI with broad-module practice behavior
- Removes concepts, question types, difficulty, and selection mode from quick mode
- Extends practice session payload/backend handling for module and topic filters

## 2026-05-25 - `188136f`

**Author:** Spiros Kontopoulos

**Full commit:** `188136fac2701bd01e1482af65b2913aafe7f1fc`

Add difficulty editing to plan preview

- Allow preview rows to edit both count and difficulty
- Detect duplicate plan rows created by difficulty changes
- Add a duplicate-resolution modal with merge, remove, and cancel actions
- Recalculate edited preview totals after duplicate resolution
- Extend Playwright coverage for editable preview behavior

## 2026-05-25 - `0c940cb`

**Author:** Spiros Kontopoulos

**Full commit:** `0c940cb9ae4b5c4e98f6ed7690b4f05f2da7d56a`

Add editable AI generation plan preview

- Add row actions to edit counts and remove preview plan rows
- Recalculate edited planned totals live against the requested count
- Disable create when customized preview totals are invalid
- Allow resetting preview edits back to the generated plan
- Add Playwright coverage for editable preview behavior

## 2026-05-25 - `e74a83c`

**Author:** Spiros Kontopoulos

**Full commit:** `e74a83c3a2a8cf6a032f12f2c57b95ef876aaa7f`

Add flexible concept targeting and live estimate tracking

- Add concept group toggles with checked and indeterminate states
- Treat topics with no selected concepts as broad topic-level targets
- Add a live target estimate card to the AI generation builder side rail
- Keep mixed broad and specific targeting covered by Playwright smoke checks

## 2026-05-25 - `12a285a`

**Author:** Spiros Kontopoulos

**Full commit:** `12a285ae57f415480c96560beb238e4555c7f053`

Support mixed topic targeting in AI generation builder

- Allow selected modules to remain broad when no specific topics are checked
- Add module-level topic toggles with checked and indeterminate states
- Route concept selection only through explicitly selected topics
- Fix preview-plan routing and broad module validation
- Add Playwright coverage for mixed broad and specific topic previews

## 2026-05-25 - `77544e2`

**Author:** Spiros Kontopoulos

**Full commit:** `77544e29a90e368e7cdeea30aa3392ea8bd0e2ca`

Polish AI generation builder step flow

- Fix Technology and Domain edit behavior
- Add Close behavior for opened completed steps
- Show a cleaner two-card upcoming-step rail
- Smooth the main step accordion transitions
- Route specific-topic plans through Concepts before Settings

## 2026-05-25 - `2887a2b`

**Author:** Spiros Kontopoulos

**Full commit:** `2887a2b405d806d8cf8bccd4a4e058fb1061b1be`

Question generation page UI - Update Scope edit and locked flow path

## 2026-05-25 - `1391d7b`

**Author:** Spiros Kontopoulos

**Full commit:** `1391d7b4889b7ec20e1b00cef1c6a6683b8e08f2`

Polish AI generation builder summary bar

- Remove the stitched connected look from the bottom summary bar
- Display summary metrics as separate rounded cards
- Make the summary bar static instead of following page scroll
- Keep the existing builder behavior unchanged

## 2026-05-25 - `750013a`

**Author:** Spiros Kontopoulos

**Full commit:** `750013a7af68ccd693245c52d4060ce793e5fd51`

Create generation plan - Fix specific topics builder flow and add Playwright coverage

- Keep the builder flow moving after selecting specific topics
- Prevent the specific-topics path from dead-ending before question types
- Add regression coverage for the staged AI generation builder flow
- Update preview smoke checks to avoid brittle difficulty assumptions

## 2026-05-25 - `e76439e`

**Author:** Spiros Kontopoulos

**Full commit:** `e76439e942cecdd546a09614bdf6d3f74550145a`

Preserve staged builder edits and polish preview pagination

- Preserve valid downstream selections when editing completed builder steps
- Reset child state only when selected scope/modules actually change
- Prune only invalid module, topic, and concept selections
- Reuse admin pagination style for numbered centered plan preview pages

## 2026-05-25 - `bfaa203`

**Author:** Spiros Kontopoulos

**Full commit:** `bfaa2030211eadc8849fe90a60bf5df0568c10c1`

Guard manual allocation in staged builder

- Disable manual allocation for staged grouped generation plans
- Keep Equal, Random, and Weighted allocation available
- Prevent invalid grouped manual payloads from reaching the backend
- Reserve manual allocation for a future per-target count table

## 2026-05-25 - `45d91b5`

**Author:** Spiros Kontopoulos

**Full commit:** `45d91b56e2208df99b1b5c572e461ad4fabc7169`

Polish AI generation builder icons and card states

- Add reusable builder icon components for status and summary UI
- Improve locked card icon placement and locked-state labels
- Add technology-specific Python icon treatment
- Polish warning, lock, and summary bar icon visuals

## 2026-05-25 - `dffcf26`

**Author:** Spiros Kontopoulos

**Full commit:** `dffcf26c15235ba283677b7287c83e73be3e6ba4`

Icons polish - UI generative creation page

## 2026-05-25 - `c273a16`

**Author:** Spiros Kontopoulos

**Full commit:** `c273a16f98c2383386d163620ed4a6b2b36ebf30`

Allow staged builder preview with multiple targets

- Allow multi-topic staged AI generation payloads in backend validation
- Treat requested count below estimated targets as a warning instead of a blocker
- Keep all-concepts selection valid for the builder flow
- Enable Review Plan for valid multi-module and multi-topic selections

## 2026-05-25 - `0f25bd5`

**Author:** Spiros Kontopoulos

**Full commit:** `0f25bd5cbe4c7cfb8e9f791a857141b20bfb6671`

Polish AI generation builder template styling

- Align progress bar, side cards, and summary bar closer to the target template
- Add editable applied step actions and downstream reset behavior
- Add visual status icons for completed, warning, and locked states
- Preserve the staged builder flow and per-module question type matrix

## 2026-05-25 - `5f45fad`

**Author:** Spiros Kontopoulos

**Full commit:** `5f45fad878501e42c965be1a484a7f28151b68d4`

Align AI generation builder layout structure

- Move active builder steps into the main workspace
- Add right-side step rail for upcoming locked stages
- Keep Step 1 focused on Technology and Domain selection
- Preserve staged builder logic, matrix selection, and preview/create behavior

## 2026-05-24 - `22ae391`

**Author:** Spiros Kontopoulos

**Full commit:** `22ae391d967f9f131390c808f6b39e9926dd2d94`

Polish AI generation settings and readiness flow

- Add assessment settings overview and readiness validation
- Disable preview and create until required builder stages are applied
- Improve summary bar guidance and next-action messaging
- Polish validation for requested count, difficulties, and allocation strategy

## 2026-05-24 - `1d4ec24`

**Author:** Spiros Kontopoulos

**Full commit:** `1d4ec242787b427a16e415746362c7c332b64e31`

Add topics and concepts refinement steps

- Add grouped topic selection for specific-topic generation mode
- Add optional concept refinement grouped under applied topics
- Lock later builder steps until required topic/concept state is applied
- Update builder step descriptions and summary text

## 2026-05-24 - `c9f2343`

**Author:** Spiros Kontopoulos

**Full commit:** `c9f23437d1460a2ef8d833e42551ad1216d90c8d`

Polish question type matrix cell states

- Change available matrix cells to neutral grey
- Change disabled matrix cells to yellow-orange warning styling
- Keep selected cells green for clear selected state
- Remove duplicate disabled cell styling that overrode the intended colors

## 2026-05-24 - `973ff0e`

**Author:** Spiros Kontopoulos

**Full commit:** `973ff0ed3b4f2cf940622bd8665c70b37313c80a`

Add per-module question type matrix

- Add module/question-type matrix for AI generation planning
- Allow valid question type cells to be selected per module
- Keep invalid module/question-type combinations disabled per cell
- Require applied question type selections before unlocking later builder steps

## 2026-05-24 - `0741747`

**Author:** Spiros Kontopoulos

**Full commit:** `0741747d9ca0e873b12335df4592a9d812d53af1`

Add AI generation module selection step

- Add module checkbox selection after scope is applied
- Add select all and deselect all module actions
- Add topic mode choice for later topic refinement
- Require applied modules before unlocking eligible question types

## 2026-05-24 - `2ac64d7`

**Author:** Spiros Kontopoulos

**Full commit:** `2ac64d7693a799a1fbe7dc05e07b359d572298c1`

Add AI generation scope lock flow

- Add applied Technology and Domain scope state
- Add Apply Scope and Edit Scope actions
- Lock downstream builder cards until scope is applied
- Update stepper and summary bar states for the staged builder flow

## 2026-05-24 - `d512863`

**Author:** Spiros Kontopoulos

**Full commit:** `d5128635aa14ae6f81fbff86a310cd20330a542c`

Add AI generation builder layout foundation

- Add staged builder page structure for AI generation creation
- Add stepper, builder cards, and bottom summary bar
- Preserve the existing working generation flow during the layout transition
- Keep eligibility-filtered question type loading intact

## 2026-05-24 - `69b282e`

**Author:** Spiros Kontopoulos

**Full commit:** `69b282e7b099962315e984c3ec1e2ccb67df2b14`

Remove unused legacy question type mapping helpers

- Remove old Language/Category question type mapping API helpers
- Keep the new module eligibility lookup helper
- Preserve the active question type mappings route as the new eligibility view
- Leave backend legacy compatibility routes untouched

## 2026-05-24 - `76d20b8`

**Author:** Spiros Kontopoulos

**Full commit:** `76d20b8865279ca5f1810ea58fe04d81e8f1a415`

Replace question type mapping page with eligibility view

- Replace legacy Language/Category mapping UI with module eligibility inspection
- Show Technology Module to Question Type eligibility from the new endpoint
- Support technology, domain, and module-level inspection
- Keep the first version read-only while preserving legacy backend routes

## 2026-05-24 - `7d08422`

**Author:** Spiros Kontopoulos

**Full commit:** `7d08422576a960d4052aea59f99de1bb4c3a57e3`

Enforce question type eligibility in AI planner

- Validate module/question-type eligibility during AI generation planning
- Inherit eligibility from parent modules for selected topics and concepts
- Reject invalid module/question-type combinations with clean 400 errors
- Keep legacy Language/Category question type validation untouched

## 2026-05-24 - `84d8dc8`

**Author:** Spiros Kontopoulos

**Full commit:** `84d8dc867c288534647bf98cc8c6f7e1339db968`

Filter AI generation question types by eligibility

- Add frontend lookup support for module/question-type eligibility
- Load eligible question types from the new taxonomy endpoint
- Reconcile selected question types when taxonomy scope changes
- Prevent invalid question type selections on the AI generation create page

## 2026-05-24 - `fa2be7a`

**Author:** Spiros Kontopoulos

**Full commit:** `fa2be7ab7f1d6827c6e970eaeba3f0ec1698abd5`

Add question type eligibility lookup endpoint

- Add REST endpoint for module/question-type eligibility lookup
- Resolve eligible question types by technology, domain, or module scope
- Return module metadata for each eligible question type
- Keep legacy question type mapping routes untouched

## 2026-05-24 - `607861e`

**Author:** Spiros Kontopoulos

**Full commit:** `607861e7017c0be5d8cf96bdda2180ce5e542874`

Seed module question type eligibility mappings

- Add initial Python module/question-type eligibility mapping rules
- Seed active mappings into the new eligibility table idempotently
- Keep select-all-that-apply disabled until the format is fully supported
- Preserve the legacy Language/Category question type mapping flow for now

## 2026-05-24 - `42c13e0`

**Author:** Spiros Kontopoulos

**Full commit:** `42c13e0dcacc73b0d945b1f54777f7d037a359db`

Add module question type eligibility model

- Add module/question-type eligibility mapping model
- Add Alembic migration for the new eligibility table
- Keep legacy Language/Category mapping structures untouched
- Prepare backend foundation for module-scoped question type filtering

## 2026-05-24 - `48b0374`

**Author:** Spiros Kontopoulos

**Full commit:** `48b03743723e4f394a077748924a97c910216829`

Remove dead quiz lookup helpers

- Remove unused legacy lookup types and helper functions from the quiz API client
- Keep active quiz CRUD and attempt APIs unchanged
- Leave admin lookup helpers intact because question type mapping still uses them
- Confirm the frontend production build still passes

## 2026-05-24 - `96679c4`

**Author:** Spiros Kontopoulos

**Full commit:** `96679c4679fadeff808b61c0491e486d70870aee`

Remove legacy taxonomy admin pages

- Remove obsolete Language, Category, and Topic taxonomy admin pages from the frontend
- Delete legacy taxonomy routes from the admin router
- Keep backend lookup APIs and database tables untouched for compatibility
- Confirm the frontend production build still passes

## 2026-05-24 - `bf2331f`

**Author:** Spiros Kontopoulos

**Full commit:** `bf2331f9521d2ac2ce0653826e04922840e303c8`

Update dashboard taxonomy coverage

- Replace legacy lookup coverage with technology taxonomy coverage
- Show field, technology, domain, module, topic, and concept counts
- Keep question type coverage visible as assessment metadata
- Leave legacy lookup tables and backend routes untouched during migration

## 2026-05-24 - `950d787`

**Author:** Spiros Kontopoulos

**Full commit:** `950d7871881d9aa0bae17b6cebf58642297be09f`

Remove visible legacy taxonomy UI

- Redirect legacy taxonomy admin routes back to the active Technology Taxonomy page
- Remove legacy Language, Category, and Topic cards from the taxonomy landing page
- Keep backend lookup routes and database tables untouched for compatibility
- Confirm the frontend production build still passes

## 2026-05-24 - `5daac77`

**Author:** Spiros Kontopoulos

**Full commit:** `5daac771baba83171023969b7ef38e1c6fe6a375`

Isolate legacy taxonomy admin screens

- Point the main admin taxonomy navigation to the new Technology Taxonomy page
- Move legacy Language, Category, and Topic screens away from the active taxonomy workflow
- Add legacy compatibility messaging for old lookup-management pages
- Keep backend lookup routes and database tables unchanged during the migration

## 2026-05-24 - `c8ec2c7`

**Author:** Spiros Kontopoulos

**Full commit:** `c8ec2c75ed390a1e687a9598744219857e06d2d0`

Migrate admin question filters to new taxonomy

- Replace legacy language/category/topic filters with technology taxonomy filters
- Update admin question list filtering to use technology, domain, module, topic, and concept
- Update quiz question picker filters to match the new taxonomy structure
- Keep question type as separate assessment metadata
- Verify admin question browsing, quiz creation, and quiz running with the new filters

## 2026-05-24 - `47fca05`

**Author:** Spiros Kontopoulos

**Full commit:** `47fca05f93f44cf2677346cf17cff134742bdbbe`

Migrate practice flow to new taxonomy filters

- Update practice selection schemas and queries to use technology/domain/module/topic filters
- Store and return new taxonomy filters on practice sessions
- Update the public practice page to select the new taxonomy path
- Disable legacy sample question seeding after the taxonomy migration
- Return clean 400 responses for invalid practice selection filters

## 2026-05-24 - `2588808`

**Author:** Spiros Kontopoulos

**Full commit:** `2588808efa0cf137c1536abfcac24c86381fdbd8`

Add dev content reset script

- Add a dev-only SQL script for wiping disposable content/runtime data
- Preserve schema, migrations, taxonomy/reference data, and question types
- Reset questions, quizzes, practice sessions, attempts, and AI generation drafts
- Document the local Docker Compose command for running the reset

## 2026-05-24 - `cf8a711`

**Author:** Spiros Kontopoulos

**Full commit:** `cf8a7113c88282c69e2e8a9dc97e912b16ba9deb`

Update dashboard taxonomy health checks

- Replace legacy missing language/category/topic dashboard warnings with new taxonomy health warnings
- Count missing technology, domain, module, and technology topic references
- Keep legacy lookup coverage visible but clearly labeled as migration scaffolding
- Update frontend dashboard types and warning labels for B3 cleanup tracking

## 2026-05-24 - `9e141d4`

**Author:** Spiros Kontopoulos

**Full commit:** `9e141d4d18e8e06066e9752d0b71009d52201740`

Target AI generation with new taxonomy

- Replace legacy generation targeting with Technology, Domain, Module, Topic and Concept fields
- Keep Question Type, Difficulty, Count and Provider as separate generation settings
- Store and display taxonomy paths on generation plans and generated drafts
- Pass taxonomy context into question-service prompt generation
- Update AI generation smoke tests for the new taxonomy-based flow

## 2026-05-23 - `8d4522b`

**Author:** Spiros Kontopoulos

**Full commit:** `8d4522bd74891b0effad3300e6555ff1f09dc38e`

Move question types under questions admin

- Add dedicated question types routes under the questions admin area
- Redirect legacy taxonomy question type routes to the new questions routes
- Add question types navigation from the admin questions page
- Remove question type cards from the taxonomy landing page
- Split question and question type styles into dedicated CSS files

## 2026-05-23 - `2b336e9`

**Author:** Spiros Kontopoulos

**Full commit:** `2b336e99f01bea6e6d7fce761be3c6fef02284e1`

Move question forms to new taxonomy

- Remove legacy language/category/topic selectors from active question create and edit forms
- Use Technology, Domain, Module, Topic and optional Concept as the content target
- Keep Question Type, Difficulty, Status and Time Limit as separate assessment metadata
- Allow backend question saves without legacy taxonomy IDs
- Preserve legacy fields internally while preparing final cleanup

## 2026-05-23 - `088a55a`

**Author:** Spiros Kontopoulos

**Full commit:** `088a55ac6b1d9e990b42f2e7db251258602801a8`

Connect questions to new taxonomy

- Add optional new taxonomy references to question API handling
- Validate Technology, Domain, Module, Topic and Concept parent consistency
- Add taxonomy selector support to admin question create and edit pages
- Show assigned taxonomy path in admin question list and detail views
- Keep legacy taxonomy fields compatible while preparing migration

## 2026-05-23 - `7a38a6f`

**Author:** Spiros Kontopoulos

**Full commit:** `7a38a6f22af8eef5cd0fc6e616ca3f8993155a0d`

Admin taxonomy new css file

## 2026-05-23 - `9645dbb`

**Author:** Spiros Kontopoulos

**Full commit:** `9645dbb6e5feea1e8f60689c2f7cf272bb72bf73`

Admin taxonomy UI polish v2

## 2026-05-23 - `4dca761`

**Author:** Spiros Kontopoulos

**Full commit:** `4dca7617ee12fd9fb4137008523ea029910da3c6`

Admin taxonomy UI polish

## 2026-05-23 - `d7ed516`

**Author:** Spiros Kontopoulos

**Full commit:** `d7ed5165f15c6cafb6ef263558d38edb977f70a8`

Add admin taxonomy CRUD

- Add create and update schemas for taxonomy entities
- Add taxonomy create, edit, deactivate and reactivate API actions
- Extend the admin taxonomy page with CRUD controls
- Refresh the taxonomy tree after changes
- Keep taxonomy deletion soft through active/inactive state

## 2026-05-23 - `69a9e49`

**Author:** Spiros Kontopoulos

**Full commit:** `69a9e4977cd29fcc365ae028a5b157d025fc00c4`

Add admin taxonomy viewer

- Add read-only admin page for the new Python taxonomy tree
- Fetch taxonomy data from the backend taxonomy API
- Show expandable Field/Technology/Domain/Module/Topic/Concept structure
- Add selected entity details and taxonomy summary counts
- Keep the viewer read-only before connecting taxonomy to generation and questions

## 2026-05-23 - `2d56663`

**Author:** Spiros Kontopoulos

**Full commit:** `2d566634872deab87fe96bd2d925de6e971a13b2`

Add Python taxonomy foundation

- Add Field, Technology, Domain, Module, Topic and Concept taxonomy models
- Add Alembic migration for taxonomy tables and future taxonomy references
- Seed Python taxonomy with domains, modules, topics, concepts and ecosystem libraries
- Expose read-only taxonomy tree API for future admin/public UI
- Keep existing language/category/topic flows compatible

## 2026-05-23 - `7c40982`

**Author:** Spiros Kontopoulos

**Full commit:** `7c40982382fee79dfe6cceeacef0138ff299a168`

Add question timestamps to admin questions

- Add created_at and updated_at fields to questions
- Add Alembic migration for question timestamp columns
- Expose timestamps through question schemas and API sorting
- Show Created date in the admin questions table
- Support sorting questions by created date

## 2026-05-23 - `1dcb60d`

**Author:** Spiros Kontopoulos

**Full commit:** `1dcb60da54a79f19d17d2a724a99e7f0d49be151`

Add sorting and pagination to admin tables

- Adds sortable admin table headers for reusable list/table screens
- Adds question ID display and backend sorting to the admin questions list
- Adds pagination and sorting to the AI generation batches list
- Reuses shared admin pagination controls where practical
- Fixes backend query import aliasing for FastAPI sort parameters

## 2026-05-22 - `09a0c30`

**Author:** Spiros Kontopoulos

**Full commit:** `09a0c3044ece728abdd335dd5eecb1ac9d2cf768`

Improve AI draft duplicate review UI

- Adds clearer duplicate-warning badges and grouped validation notes for generated drafts
- Uses click-to-open draft previews instead of hover-based expansion
- Separates review metadata from question content in the draft preview
- Keeps approved question links visible beside approved draft status
- Makes bulk approve skip duplicate-warning drafts while marking them for later review

## 2026-05-22 - `11bd99f`

**Author:** Spiros Kontopoulos

**Full commit:** `11bd99f4528706358b3bba83f70c224c27c793d3`

Improve AI draft duplicate review workflow

- Groups duplicate warnings and links related approved questions from the review preview
- Adds visible duplicate-warning badges to generated draft rows
- Replaces hover preview behavior with a click-based accordion for stable review interactions
- Makes bulk approve skip duplicate-warning drafts while keeping manual review available
- Allows failed or partially failed generation batches to be rerun when plan items remain

## 2026-05-22 - `f963e74`

**Author:** Spiros Kontopoulos

**Full commit:** `f963e7471721e21bb5771d475f1efe74060c1150`

Add AI generated question duplicate warnings

- Adds deterministic duplicate checks for generated AI drafts
- Compares drafts against approved questions and same-batch drafts
- Stores duplicate and near-duplicate warnings in validation errors
- Keeps duplicate detection warning-only for the first version

## 2026-05-22 - `53c41e8`

**Author:** Spiros Kontopoulos

**Full commit:** `53c41e84a6ac8f0ebfd27b4aea5192dc3ad856b5`

Add static AI prompt quality rules

- Adds versioned prompt rules for model profiles, difficulties, and question types
- Passes question type codes from quiz-api to question-service for reliable rule selection
- Stores the active prompt version on generated batches
- Adds safe local environment template for OpenAI generation settings

## 2026-05-22 - `d5523ba`

**Author:** Spiros Kontopoulos

**Full commit:** `d5523baf3cde8a53e6ace422842b8dc6100749b0`

Add AI generated draft edit workflow

- Adds backend support for editing staged AI generated drafts before approval
- Adds admin edit modal for prompt, code snippet, explanation, timer, answer options, and review notes
- Revalidates edited drafts before saving and approval
- Extends Playwright smoke coverage to edit and approve a generated draft

## 2026-05-22 - `1ed9889`

**Author:** Spiros Kontopoulos

**Full commit:** `1ed98895dffbfaf7703bae87f18f33afa5e96125`

Update AI generation smoke test for new run controls

- Removes stale provider select assertion
- Keeps mock generation as the safe Playwright path
- Verifies generated draft preview and bulk approval still work

## 2026-05-22 - `8b6f344`

**Author:** Spiros Kontopoulos

**Full commit:** `8b6f344b38a64c2aea3a9c2f8cb3ce2fb43d3158`

Add AI generation cost estimate and safer run controls

- Adds pre-run OpenAI cost estimation for AI generation batches
- Moves real Gen AI execution behind a confirmation modal with estimate details
- Simplifies batch detail actions with separate mock and Gen AI run controls
- Improves batch summary layout for plan, review, execution, and cost metadata
- Adds shared admin back-link and confirmation modal components

## 2026-05-22 - `fa8203b`

**Author:** Spiros Kontopoulos

**Full commit:** `fa8203bfc77b85d7f412f0b45a7d238391367380`

Restore AI generation provider controls

- Restores provider and model profile controls on the AI generation detail page
- Preserves provider/model/cost metadata display
- Keeps shared multiline answer option rendering in AI draft previews
- Fixes the admin AI generation Playwright smoke flow

## 2026-05-21 - `6388408`

**Author:** Spiros Kontopoulos

**Full commit:** `6388408b5078198f6b7845ef8d415aece350b1ac`

Improve multiline answer option rendering

- Adds shared answer option text renderer for multiline/code-like answers
- Converts admin answer option fields from inputs to textareas
- Preserves line breaks in admin, quiz, and practice answer displays
- Handles AI-generated output answers with real or escaped newline characters

## 2026-05-21 - `30c4c6f`

**Author:** Spiros Kontopoulos

**Full commit:** `30c4c6f1b00c5c8a7d379e954728cac215915881`

Temporary fix for new line characters in admin UI

## 2026-05-21 - `6d18b89`

**Author:** Spiros Kontopoulos

**Full commit:** `6d18b8972b17d74e7ad7b5808f06edf843e7b64d`

Track AI generation provider model and cost

- Adds provider, execution mode, model profile, and model used tracking
- Records OpenAI token usage and calculated generation cost
- Shows AI execution and cost metadata in the admin generation review flow
- Keeps mock generation as the default safe path for tests and local demos

## 2026-05-21 - `5a54771`

**Author:** Spiros Kontopoulos

**Full commit:** `5a54771081e43ed6292647037be0e2b1cc029926`

Add real OpenAI generation provider

- Adds OpenAI-backed question generation endpoint with structured output validation
- Keeps mock generation as the default safe provider
- Lets quiz-api run AI batches using mock or OpenAI providers
- Stores real OpenAI output through the existing staged review workflow

## 2026-05-21 - `6df5ee6`

**Author:** Spiros Kontopoulos

**Full commit:** `6df5ee614ce093ffb59cc6935f4644b87a57343b`

Rename and move admin-ai-generation-detail css file

## 2026-05-21 - `5eb3788`

**Author:** Spiros Kontopoulos

**Full commit:** `5eb378884777e58722034b72c739e976f230607a`

Add bulk generated draft review workflow

- Add paginated generated draft loading for AI generation batches
- Add reusable admin pagination and hover accordion components
- Replace one-by-one review with fast hover preview and local decisions
- Add visible-page approve/reject marking and bulk apply workflow
- Extend Playwright smoke coverage for generated draft review

## 2026-05-21 - `1aa873e`

**Author:** Spiros Kontopoulos

**Full commit:** `1aa873e94dea7072d12d7ffaa582438ab6c7089f`

Add bulk generated draft review workflow

- Add paginated generated draft loading for AI generation batches
- Add reusable admin pagination and hover accordion components
- Replace one-by-one review UI with fast hover preview and local decisions
- Add bulk generated draft review endpoint for approve/reject decisions
- Update Playwright smoke coverage for the bulk review flow

## 2026-05-21 - `86b2603`

**Author:** Spiros Kontopoulos

**Full commit:** `86b26035c4f8ebd877f317a89757cae88c676455`

Add generated draft review foundation

- Add approve and reject endpoints for AI generated drafts
- Copy approved drafts into the reusable question bank
- Add generated question review panel with answer options and code snippets
- Update batch approved/rejected counters after review actions
- Extend Playwright smoke coverage for generated draft approval

## 2026-05-21 - `7215169`

**Author:** Spiros Kontopoulos

**Full commit:** `7215169ce53b1f6525feed6b9d450e78401e39ac`

Add question-service mock generation flow

- Add mock generation endpoint to question-service
- Add quiz-api batch run endpoint for planned AI generation batches
- Store generated draft questions and answer options in AI staging tables
- Add admin detail action for running mock generation
- Add Playwright smoke coverage for the generation run flow

## 2026-05-21 - `441f22a`

**Author:** Spiros Kontopoulos

**Full commit:** `441f22a8323ffaaf5877f5a082ca7be93bf745ae`

Add question-service mock generation contract

- Add mock generation endpoint to question-service
- Add quiz-api run endpoint for planned AI generation batches
- Store mock generated drafts and answer options in AI staging tables
- Add admin batch detail run action and generated draft display
- Fix AI generation create page TypeScript narrowing

## 2026-05-20 - `e2bd059`

**Author:** Spiros Kontopoulos

**Full commit:** `e2bd059d2fd8523659c3a5e2f64971461ed60611`

Add Playwright smoke test foundation

- Add Playwright configuration and test scripts
- Add first smoke tests for API health and admin AI generation pages
- Document local E2E test commands
- Clean stale AI generation admin routes

## 2026-05-20 - `9b3a595`

**Author:** Spiros Kontopoulos

**Full commit:** `9b3a595c31263ccbcf82b41eae3b92fd6b97062a`

Add AI generation create and detail admin pages

- Split AI generation admin routes into list, create, and detail pages
- Add create-plan UI with preview, allocation options, and taxonomy selections
- Add dedicated batch detail view with paginated plan items
- Keep saved generation batches as reusable history for future clone and rerun flows

## 2026-05-20 - `50532cf`

**Author:** Spiros Kontopoulos

**Full commit:** `50532cf66b524d99073f18a487a5b1490bf7706e`

Admin UI for creating the GEN AI request formula

## 2026-05-20 - `576c030`

**Author:** Spiros Kontopoulos

**Full commit:** `576c0308f611b5310dad3c01574b74de50b00a0b`

Add admin AI generation batch page

- Add frontend API client for AI generation batch endpoints
- Add admin page for listing and inspecting planned generation batches
- Show batch plan items and generated-question placeholders
- Wire admin navigation to the AI generation route

## 2026-05-20 - `97579f0`

**Author:** Spiros Kontopoulos

**Full commit:** `97579f057a7e380b734fb1fa6fe2b505d7fe4bca`

Add AI generation admin detail endpoints

- Add batch detail endpoint with plan items and generated question summaries
- Add plan-item listing endpoint for generation batches
- Add generated-question list and detail endpoints
- Prepare backend API surface for future admin review UI

## 2026-05-20 - `3ef6c43`

**Author:** Spiros Kontopoulos

**Full commit:** `3ef6c43035244c0214adfd8bb7c630cb61e1e48e`

Add AI generation allocation strategies

- Add equal, random, weighted, and manual planning support
- Support deterministic random allocation with random seeds
- Normalize selected generation groups into clean plan items
- Keep AI execution separate from backend planning logic

## 2026-05-20 - `6d253e1`

**Author:** Spiros Kontopoulos

**Full commit:** `6d253e14736e6a77c5112364f94f0d0355b1defa`

Add AI generation planning API

- Add plan preview endpoint for AI generation batches
- Add batch creation and listing endpoints
- Store normalized generation plan items before model execution
- Keep OpenAI execution outside quiz-api for future question-service integration

## 2026-05-20 - `ccd86e7`

**Author:** Spiros Kontopoulos

**Full commit:** `ccd86e78d0337bea7299a6c15f9047091a590051`

Add AI generation staging schema

- Add AI generation batch, plan item, draft question, and draft answer models
- Support flexible generated-question allocation through plan items
- Add Alembic migration for AI staging tables
- Keep generated AI content separate from approved question-bank records

## 2026-05-20 - `81aa306`

**Author:** Spiros Kontopoulos

**Full commit:** `81aa306cff5f4b9d76b76a7e33f596aefdf79dbc`

Add Alembic migration foundation

- Add Alembic configuration for quiz-api schema migrations
- Create initial baseline migration for the current database model state
- Remove startup-time create_all schema creation from the FastAPI lifespan
- Keep lookup seeding during startup while schema changes move to migrations

## 2026-05-20 - `d9d0df8`

**Author:** Spiros Kontopoulos

**Full commit:** `d9d0df84e6a9df120e12404caa22f11076f02271`

Persist static quiz attempts

- Add anonymous static quiz attempt and answer models
- Add backend endpoints to start, answer, complete, abandon, and review quiz attempts
- Save static quiz answers immediately on click from the public quiz UI
- Add static quiz attempt metrics to the admin dashboard

## 2026-05-20 - `36d02b6`

**Author:** Spiros Kontopoulos

**Full commit:** `36d02b6194ce47ba15feaeed5def59f70e35da78`

Add static quiz answer transition lock

- Add a short click-lock after one-by-one timed answers
- Prevent accidental double-clicks from answering the next question
- Add slide-in transition between static quiz questions
- Add light hover polish for active question cards

## 2026-05-20 - `ecd704e`

**Author:** Spiros Kontopoulos

**Full commit:** `ecd704ed912446972eba462db940841a15d6b26b`

Neutralize static quiz review cards

- Remove green and red backgrounds from static quiz review question cards
- Keep review answer rows visually neutral
- Preserve result status through pills and answer labels
- Keep focused review jump highlight unchanged

## 2026-05-20 - `2abef0e`

**Author:** Spiros Kontopoulos

**Full commit:** `2abef0e0e3b6f54c2702f3dbd80deeba51722537`

Polish static quiz review answer labels

- Keep review answer rows visually neutral
- Move correct and selected-answer labels to the right side
- Avoid duplicate labels when the selected answer is correct
- Use label text color instead of row background color for answer status

## 2026-05-20 - `adc4f81`

**Author:** Spiros Kontopoulos

**Full commit:** `adc4f8137ae928040f0e4ca278563b300d973c05`

Make answer clicks final across practice and quizzes

- Submit practice answers immediately on answer click
- Pause practice total timer after answered questions until continuing
- Remove static quiz answer-behavior option and make answer clicks final
- Fix static quiz review coloring and add wrong-answer jump navigation

## 2026-05-20 - `b6fead4`

**Author:** Spiros Kontopoulos

**Full commit:** `b6fead4710ae4c0ac7b29b281aec0f0174a7c6ae`

Add configurable static quiz attempt flow

- Add quiz setup options for question view, answer behavior, and timer mode
- Hide static quiz feedback until final results
- Add score summary, timing metrics, and paginated review
- Polish public quiz cards around starting curated quiz attempts

## 2026-05-19 - `6806068`

**Author:** Spiros Kontopoulos

**Full commit:** `680606861ec8e4df6cf2231b47e9b4f690937767`

Polish practice wrong-answer navigation

- Restyle jump-to-wrong control as a compact review pill
- Align pagination controls with count and wrong-answer jump areas
- Replace repeated card action text with a tooltip icon button
- Keep wrong-answer navigation behavior unchanged

## 2026-05-19 - `333ce7e`

**Author:** Spiros Kontopoulos

**Full commit:** `333ce7ed0352dbd294f4ad32675955d2de70407e`

Add practice result paging and wrong-answer jumps

- Paginate practice review results to avoid long result pages
- Add jump-to-wrong-answer navigation across review pages
- Highlight the focused wrong answer after jumping
- Move post-session actions into the result header action area

## 2026-05-19 - `ab91d9f`

**Author:** Spiros Kontopoulos

**Full commit:** `ab91d9fbec0f5844ed4e0a1c875e2eb86102cb69`

Add live practice timers

- Add live session and current-question timers during practice
- Freeze answered question time after submission
- Show formatted total answered time in result summary
- Add average answered-question time alongside per-question review timing

## 2026-05-19 - `e4a7e7e`

**Author:** Spiros Kontopoulos

**Full commit:** `e4a7e7eccd549b2e6e2c975df8cc6aae9e56eec5`

Complete public practice session lifecycle

- Add abandoned session status and stop-session flow
- Return result summaries with per-question review data
- Show selected answer, correct answer, explanation, and time spent in review
- Preserve submitted attempts when users stop before completing practice

## 2026-05-19 - `4d858c3`

**Author:** Spiros Kontopoulos

**Full commit:** `4d858c39e455e6ffffe0db487ae6ba216b631e6e`

Add real admin dashboard stats

- Add backend dashboard stats endpoint for questions, quizzes, taxonomy, and practice activity
- Add frontend dashboard API client and replace placeholder dashboard values
- Show content readiness and missing-taxonomy warning metrics
- Add dashboard layout styles for stat cards, readiness blocks, and warning rows

## 2026-05-19 - `48dedb9`

**Author:** Spiros Kontopoulos

**Full commit:** `48dedb9d7900ba5db69ac6d70058288bd3f793e3`

Harden admin question taxonomy validation

- Validate active taxonomy combinations on question creation
- Require active language/category/topic/type mappings when taxonomy changes
- Preserve editability for existing questions with unchanged inactive taxonomy
- Show inactive lookup labels in the admin question edit form

## 2026-05-19 - `c5a6306`

**Author:** Spiros Kontopoulos

**Full commit:** `c5a630655f0542aebe7dc6048c710a8cc20a3a04`

Add question type search and pagination / Move question type mappings to dedicated page

## 2026-05-19 - `a6b7e7e`

**Author:** Spiros Kontopoulos

**Full commit:** `a6b7e7e66c8eb4b8f65193142a3f3a0937475b50`

Add question type mapping management

- Add backend endpoints for language/category question type mappings
- Add admin API helpers for fetching and saving mapping rows
- Extend question type taxonomy UI with enable/recommend/position controls
- Add supporting admin styles for the new mapping section

## 2026-05-19 - `c17d2d3`

**Author:** Spiros Kontopoulos

**Full commit:** `c17d2d35a1caf4f797b382686150a32bb78c905a`

Harden practice selection against inactive taxonomy

- Filtered practice question selection by active taxonomy state
- Treated child topics under inactive groups as unavailable
- Rejected manually submitted topic filters hidden by inactive groups
- Kept admin inactive taxonomy visibility unchanged
- Preserved existing question-bank records without mutation

## 2026-05-19 - `6953f17`

**Author:** Spiros Kontopoulos

**Full commit:** `6953f171c23c207f3535ff1b3391ef985fba7491`

Refine taxonomy action message variants

- Made reactivation messages use green success styling
- Kept deactivation messages in amber warning/info styling
- Added explicit message variants for category and topic actions
- Preserved active/inactive badge colors separately from action feedback

## 2026-05-19 - `0e3cc46`

**Author:** Spiros Kontopoulos

**Full commit:** `0e3cc469a67e8a585ea97bb14a98e277b1ca3071`

Polish category and topic taxonomy management UX

- Moved taxonomy action messages next to affected rows/cards
- Improved active and inactive badge styling
- Added topic status filtering in taxonomy management
- Marked child topics hidden by inactive parent groups
- Avoided cascading child-topic state changes when groups are deactivated

## 2026-05-19 - `b7c48b7`

**Author:** Spiros Kontopoulos

**Full commit:** `b7c48b719e39ef8989a4fce9b090e0fde23f6562`

Add category and topic taxonomy management

- Added category create/edit/deactivate workflows
- Added topic group and selectable topic management
- Added backend endpoints for category and topic mutations
- Added flat topic lookup for admin management views
- Preserved deactivate/reactivate behavior instead of hard deletion

## 2026-05-19 - `e0de315`

**Author:** Spiros Kontopoulos

**Full commit:** `e0de31501acf4789437b255bd4e1076495b92432`

Show inactive taxonomy context in admin questions

- Included inactive taxonomy records in admin question filters
- Labelled inactive lookup options in the Questions admin page
- Added warning badges for questions linked to inactive taxonomy
- Preserved existing questions for admin review instead of hiding them
- Kept public and practice flows active-taxonomy-only by default

## 2026-05-19 - `c92328b`

**Author:** Spiros Kontopoulos

**Full commit:** `c92328b1fbf3ec067b09fc9bb7df0c5618b63112`

Add taxonomy language and question type management

- Added Taxonomy link to the admin sidebar
- Added create/edit/deactivate workflows for languages
- Added create/edit/deactivate workflows for question types
- Added backend lookup mutation endpoints
- Kept public lookup endpoints active-only by default

## 2026-05-19 - `523a409`

**Author:** Spiros Kontopoulos

**Full commit:** `523a4090f5a0610700b6d8b32a26155c6820fe28`

Add admin taxonomy browse pages

- Added read-only taxonomy overview and browse routes
- Added language, category, topic, and question type browse pages
- Reused existing relationship-aware lookup endpoints
- Displayed topic groups and selectable child topics clearly
- Left taxonomy create/edit/archive actions disabled for later CRUD

## 2026-05-19 - `5f1f468`

**Author:** Spiros Kontopoulos

**Full commit:** `5f1f4681865414d60a7f3e9b7945e8f1e9fa0879`

Add search and pagination to quiz question picker

- Added search input to the quiz question-bank picker
- Reused paginated question search endpoint for picker results
- Added rows-per-page and previous/next controls
- Kept select-all scoped to visible unattached questions
- Left attached quiz questions unpaginated for easier ordering

## 2026-05-19 - `756fc24`

**Author:** Spiros Kontopoulos

**Full commit:** `756fc2406463fce0e8e13a86b0a0604636c87e2f`

Add admin question search and pagination

- Added paginated question search endpoint while keeping list endpoint compatible
- Added search box to admin Questions browse page
- Added rows-per-page and previous/next pagination controls
- Kept select-all behavior scoped to visible page results
- Reused existing taxonomy filters with paginated results

## 2026-05-19 - `7532733`

**Author:** Spiros Kontopoulos

**Full commit:** `7532733aac40868d68dcc7a99497747523de78ad`

Add admin question detail page

- Added question detail route for full question-bank records
- Linked Browse Questions View action to the detail page
- Displayed answer options, correct answer, explanation, and metadata
- Added edit and archive actions from the detail page
- Reused existing question fetch and status update APIs

## 2026-05-19 - `a77e5a9`

**Author:** Spiros Kontopoulos

**Full commit:** `a77e5a9eeb384fb3450162d04190c44ae1f38668`

Add select all controls to quiz question management

- Added select-all visible control for attached quiz questions
- Supported bulk removal without selecting each question manually
- Kept question-bank picker selection limited to visible available rows
- Used pagination-friendly wording for future paged results

## 2026-05-19 - `489631a`

**Author:** Spiros Kontopoulos

**Full commit:** `489631af8519c430d6b619a88d3754b20b6b762d`

Add quiz question ordering controls

- Added backend endpoint for static quiz question ordering
- Validated submitted order against attached quiz questions
- Updated quiz_questions position values from admin actions
- Added Move up and Move down controls to attached questions
- Preserved reusable question-bank records during reordering

## 2026-05-18 - `df39bd6`

**Author:** Spiros Kontopoulos

**Full commit:** `df39bd6e2c72ae7f0accae41b81906dd7ce7484e`

Add admin CRUD foundation for questions and quizzes

- Added question edit route and backend update endpoint
- Added question archive and bulk archive actions
- Added quiz metadata edit and quiz delete support
- Preserved question-bank records when deleting quizzes
- Updated admin APIs and shared admin styling

## 2026-05-18 - `bbe9f36`

**Author:** Spiros Kontopoulos

**Full commit:** `bbe9f36ee9c710c6ea624f5d0915ccfc52016bde`

Add quiz question detach management

- Added backend endpoint to remove quiz/question links
- Kept removed questions in the reusable question bank
- Added single and bulk remove actions for attached quiz questions
- Re-compacted quiz question positions after removal
- Updated quiz management UI with clearer detach wording

## 2026-05-18 - `19ebd27`

**Author:** Spiros Kontopoulos

**Full commit:** `19ebd27b3b3ccc0a765e7e4491de04e2b3a84812`

Refactor quiz question management into picker mode

- Replaced quiz-specific question creation with question-bank picker
- Added attached questions section for static quizzes
- Added filterable question-bank selection inside quiz management
- Wired existing attach-question endpoint into frontend API
- Kept central question creation in the Questions admin area

## 2026-05-18 - `5e4ab26`

**Author:** Spiros Kontopoulos

**Full commit:** `5e4ab26cfb0dfcff4cdcff815dc95af7486a2b4d`

Add admin topic group question filtering

- Added topic_group_id support to question listing
- Added Topic group filter to admin question browse page
- Narrowed topic dropdown based on selected topic group
- Allowed group-level filtering across all child topics

## 2026-05-18 - `2060c0d`

**Author:** Spiros Kontopoulos

**Full commit:** `2060c0d2cb5902f25ce03ad4039b5dfea3cc290a`

Add admin question bank browse and create pages

- Added official admin Questions section
- Added question-bank browse/list page with filters
- Added question creation page using language/category/topic/type flow
- Added admin question and lookup API helpers
- Left quiz-specific question management unchanged for picker-mode refactor

## 2026-05-18 - `aa0d50a`

**Author:** Spiros Kontopoulos

**Full commit:** `aa0d50ad0e3358caffc05369276c8a2c7ccd384e`

Update static quiz manage questions

## 2026-05-18 - `ea807b7`

**Author:** Spiros Kontopoulos

**Full commit:** `ea807b7d9d670594689d32db0b009b993edf136f`

Validate practice selection taxonomy filters

## 2026-05-18 - `bce9ef2`

**Author:** Spiros Kontopoulos

**Full commit:** `bce9ef2c269de2b0593f438718fc3e829f11ebb5`

Refine practice builder preview wording

## 2026-05-18 - `cd25714`

**Author:** Spiros Kontopoulos

**Full commit:** `cd25714612dda38f9e2ac233ea857a57c3e8ebe6`

Update shortage message when filtering questions

## 2026-05-18 - `1976402`

**Author:** Spiros Kontopoulos

**Full commit:** `197640294a1b86d794d504d9860b611baccdee9c`

Polish practice builder preview and validation

## 2026-05-18 - `24756f0`

**Author:** Spiros Kontopoulos

**Full commit:** `24756f00e8725a3cf8ef9b482126889a665235af`

Add progressive practice builder filters

## 2026-05-18 - `efc787a`

**Author:** Spiros Kontopoulos

**Full commit:** `efc787a7847b6e5dc2dd206d64631fe566872f03`

Add topic-aware multi-select practice selection

## 2026-05-18 - `0b93102`

**Author:** Spiros Kontopoulos

**Full commit:** `0b931026610f98cc46e1194d77ce81ae1f1a92de`

Add relationship-aware taxonomy lookup foundation

## 2026-05-18 - `a4e839f`

**Author:** Spiros Kontopoulos

**Full commit:** `a4e839f220de3f79c99d652781b932ec9667b410`

Add practice session filter UI

## 2026-05-18 - `de0b237`

**Author:** Spiros Kontopoulos

**Full commit:** `de0b237e645d6f37f54589024ca71d3c270bf28f`

Polish frontend practice flow

## 2026-05-18 - `503a4e6`

**Author:** Spiros Kontopoulos

**Full commit:** `503a4e6a38bc264a28001dda19b5341ae65be199`

Add frontend practice answer flow

## 2026-05-18 - `23a3e98`

**Author:** Spiros Kontopoulos

**Full commit:** `23a3e9881c659459c341ea9bf58ea476983be106`

Split frontend styles by app area

## 2026-05-18 - `ec7f9eb`

**Author:** Spiros Kontopoulos

**Full commit:** `ec7f9eb79bd0f7507eef4a084685d9d5fa757a75`

Add initial frontend practice session flow

## 2026-05-18 - `89f146a`

**Author:** Spiros Kontopoulos

**Full commit:** `89f146a1f2adebec01077caefaebf0c1d802f4e6`

Add practice session completion lifecycle

## 2026-05-18 - `08df005`

**Author:** Spiros Kontopoulos

**Full commit:** `08df0057b5b689908a7d9ded8e91115a84602f07`

Return answered timestamp for question attempts

## 2026-05-18 - `4b804bc`

**Author:** Spiros Kontopoulos

**Full commit:** `4b804bc88f0ccaf3a82b6ba7c0fdaff381cf3681`

Update existing practice answer attempts

## 2026-05-18 - `22a7004`

**Author:** Spiros Kontopoulos

**Full commit:** `22a700421d0afb1c729c8d3dc742f72f8edf8c43`

Add practice session result endpoint

## 2026-05-18 - `b8a387c`

**Author:** Spiros Kontopoulos

**Full commit:** `b8a387cd50376cfd3998d53fc517a60bc274de56`

Add practice session attempts listing

## 2026-05-18 - `703e444`

**Author:** Spiros Kontopoulos

**Full commit:** `703e4442e3699c96394cb49846a121d4905bfde1`

Add practice session answer submission

## 2026-05-18 - `e7063f6`

**Author:** Spiros Kontopoulos

**Full commit:** `e7063f6d95d5af17926da729bfae3517766c9399`

Add question attempt schemas

## 2026-05-18 - `f57ee86`

**Author:** Spiros Kontopoulos

**Full commit:** `f57ee8673a4615170b7b260e42cbbde7be1dd64f`

Add question attempt model

## 2026-05-18 - `c2703d8`

**Author:** Spiros Kontopoulos

**Full commit:** `c2703d8894c8323e182f6ceb109e357f8c845c12`

Use summary response for practice session listing

## 2026-05-18 - `c635b62`

**Author:** Spiros Kontopoulos

**Full commit:** `c635b622a3e9b44a2b65e72645a4a6525bde8ae5`

Add practice session listing endpoint

## 2026-05-18 - `ff83d0c`

**Author:** Spiros Kontopoulos

**Full commit:** `ff83d0c0107270318d367410602df8da530a2758`

Persist excluded question count for practice sessions

## 2026-05-18 - `dd7044f`

**Author:** Spiros Kontopoulos

**Full commit:** `dd7044ff3f87a49a4b99450cdcee6309a33ee9fe`

Add practice session endpoints

## 2026-05-18 - `34ece3a`

**Author:** Spiros Kontopoulos

**Full commit:** `34ece3ae0d1d157711ab8964abbd7162296d3f2e`

Add practice session service

## 2026-05-18 - `8e1318e`

**Author:** Spiros Kontopoulos

**Full commit:** `8e1318e5329a0ee379553dde459483a490056be9`

Add practice session schemas

## 2026-05-18 - `6b40bfa`

**Author:** Spiros Kontopoulos

**Full commit:** `6b40bfa2667e17e429e28ea753b61df45164555c`

Add practice session models

## 2026-05-18 - `3c4505e`

**Author:** Spiros Kontopoulos

**Full commit:** `3c4505e2029155924ba86d598a793c854505cff4`

Add shortage count to question preview

## 2026-05-18 - `3efb9c4`

**Author:** Spiros Kontopoulos

**Full commit:** `3efb9c49d1a5fde4ff668c6d8df4051e4f4b0770`

Return applied filters in question preview

## 2026-05-18 - `7b5c751`

**Author:** Spiros Kontopoulos

**Full commit:** `7b5c751e405ae7a5f53fa9596c2d05eca7216868`

Return selection mode in question preview

## 2026-05-18 - `ed0f0b9`

**Author:** Spiros Kontopoulos

**Full commit:** `ed0f0b9d76836e85559ecd12fee0c685e1fcfde7`

Add selection mode to dynamic question preview

## 2026-05-18 - `14feef5`

**Author:** Spiros Kontopoulos

**Full commit:** `14feef5970ec6309d6067a4f6165e89aaf93b9e8`

Move question selection count validation to schema

## 2026-05-18 - `0e47251`

**Author:** Spiros Kontopoulos

**Full commit:** `0e47251b008cc15553207c505b020a5f7f3db504`

Extract dynamic question selection service

## 2026-05-18 - `1ea1cc0`

**Author:** Spiros Kontopoulos

**Full commit:** `1ea1cc0c00ae24c2d26bd17ed52ca41ae62d9693`

Add available count to dynamic selection preview

## 2026-05-18 - `6a3fd96`

**Author:** Spiros Kontopoulos

**Full commit:** `6a3fd9679c0a1a99f0a51440906e3fcca8ff0f8a`

Validate excluded question IDs in dynamic selection

## 2026-05-17 - `415ea9f`

**Author:** Spiros Kontopoulos

**Full commit:** `415ea9f418bcafaa49e97e59b91ef3287b859fac`

Add question exclusion to dynamic selection

## 2026-05-17 - `bbc46bd`

**Author:** Spiros Kontopoulos

**Full commit:** `bbc46bdc7b5a571b0cec15e65aabf991350c0f29`

Wrap dynamic question selection preview response

## 2026-05-17 - `7ae4c10`

**Author:** Spiros Kontopoulos

**Full commit:** `7ae4c10c15ceea2ebb0ad8ae330b86fb23a1b41b`

Add dynamic question selection preview endpoint

- Added request schema for question selection previews
- Added POST /question-selections/preview for filtered question-bank selection
- Supported language, category, subcategory, question type, difficulty, and question count filters
- Returned approved questions in random order for future practice/custom quiz flows

## 2026-05-17 - `8a348df`

**Author:** Spiros Kontopoulos

**Full commit:** `8a348dfddb1d72d759ae90840fbc456738040678`

Add question bank filtering

- Added filters to GET /questions for language, category, subcategory, question type, difficulty, and status
- Prepared question-bank endpoint for admin lists, custom quiz creation, practice sessions, and AI review workflows

## 2026-05-17 - `1008c01`

**Author:** Spiros Kontopoulos

**Full commit:** `1008c0124bdbed61eec9f8ca53f764b0dbf07701`

Validate lookup IDs during question creation

- Added shared question builder for question creation endpoints
- Validated language, category, subcategory, and question type IDs
- Auto-filled temporary compatibility string fields from lookup records
- Reused the same creation logic for standalone questions and quiz-attached questions

## 2026-05-17 - `4b61a2b`

**Author:** Spiros Kontopoulos

**Full commit:** `4b61a2bb53eb052e19bc7f403156fd925eab45e7`

Add lookup taxonomy seed data and endpoints

## 2026-05-17 - `38f0a3d`

**Author:** Spiros Kontopoulos

**Full commit:** `38f0a3dc4bbe7aa0af8f49c729d3446d8c8fda87`

Refactor quiz API to question bank architecture

## 2026-05-17 - `0eb1864`

**Author:** Spiros Kontopoulos

**Full commit:** `0eb1864a826b9d66db860f3f807489612c1eb3be`

Add admin question creation page

## 2026-05-17 - `e60a4b8`

**Author:** Spiros Kontopoulos

**Full commit:** `e60a4b8e9593c7e48b7d845f7c783761261a5a32`

Add admin quiz creation form

## 2026-05-17 - `c01d00e`

**Author:** Spiros Kontopoulos

**Full commit:** `c01d00e577a0279bac3569251aa94921b74273e2`

Add base frontend styling

## 2026-05-17 - `d2da507`

**Author:** Spiros Kontopoulos

**Full commit:** `d2da507995566a5716c1044c2592cdd8319ac42d`

Add frontend routing and page structure

## 2026-05-17 - `126d18c`

**Author:** Spiros Kontopoulos

**Full commit:** `126d18c669e827d6df6436dae4710e71f2b1bbcb`

Display quiz details in frontend

## 2026-05-17 - `1dfef48`

**Author:** Spiros Kontopoulos

**Full commit:** `1dfef48e4985f5d2d095a2a0af4b9986b852897c`

Add question creation endpoint

## 2026-05-16 - `988b738`

**Author:** Spiros Kontopoulos

**Full commit:** `988b73862f331039f47f05aadd1973fbb5325a29`

Display quizzes from API in frontend

## 2026-05-16 - `452581c`

**Author:** Spiros Kontopoulos

**Full commit:** `452581caf34bf1d8608fdd88638bbe25fd27e2e3`

Add quiz CRUD API endpoints

## 2026-05-16 - `097f69a`

**Author:** Spiros Kontopoulos

**Full commit:** `097f69a541205573867bb95bff944ff7d3699870`

Add initial quiz database models

## 2026-05-16 - `be89b9b`

**Author:** Spiros Kontopoulos

**Full commit:** `be89b9bca53159b57c1ba9af18b827dbdfa188d6`

Display database health in frontend

## 2026-05-16 - `7d4e66d`

**Author:** Spiros Kontopoulos

**Full commit:** `7d4e66df135f041103f783fb49bded74cf65acc4`

Add dependency health checks to question service

## 2026-05-16 - `9d1ee51`

**Author:** Spiros Kontopoulos

**Full commit:** `9d1ee51d7b3ebb72f7d58fbd8930b2791606cb5e`

Add PostgreSQL health check to quiz API

## 2026-05-16 - `5590f0b`

**Author:** Spiros Kontopoulos

**Full commit:** `5590f0b8eab06bf5bc5f15db552f5afbf72a7df7`

Configure frontend environment API URL

## 2026-05-15 - `4d02168`

**Author:** Spiros Kontopoulos

**Full commit:** `4d02168cdab632c976bc665ea00e9c3326db475a`

Add CORS explanation comments

## 2026-05-15 - `96ac422`

**Author:** Spiros Kontopoulos

**Full commit:** `96ac422b662926028a9dc6336f00d64c791ccaca`

Connect frontend to quiz API health endpoint

## 2026-05-15 - `ef71910`

**Author:** Spiros Kontopoulos

**Full commit:** `ef71910315cf4172b8e2ca5048f6610dd2a9004e`

Add frontend Vite React container

## 2026-05-15 - `d3c6cfe`

**Author:** Spiros Kontopoulos

**Full commit:** `d3c6cfeb94c27cd1484fefde476bfd32a8f67e4b`

Initial AI quiz platform skeleton

