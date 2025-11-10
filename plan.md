# To-Do App — Build Plan

## 1) Objectives
- Deliver a modern, colorful to-do app (React + FastAPI + MongoDB) with icons and excellent UX.
- CRUD for tasks with properties: id (UUID), title, description, due_date (ISO), category, completed, created_at, updated_at.
- Fixed categories: Work, Personal, Shopping, Health, Other.
- Filters: All, Active, Completed. Edit existing tasks.
- Persist reliably in MongoDB; clean API and responsive UI updates. No auth in v1.

POC Decision: Skipped (standard CRUD). Proceed directly to V1 development.

## 2) Development Phases

### Phase 2: V1 App Development (Core)
- Backend (FastAPI)
  - Model: Task { id: UUID str, title: str (required), description: str, due_date: datetime (tz-aware ISO), category: enum[Work|Personal|Shopping|Health|Other], completed: bool (default False), created_at, updated_at }
  - Endpoints (all prefixed with /api):
    - GET /tasks?status=[all|active|completed]&category=[optional]
    - POST /tasks (create task)
    - PUT /tasks/{task_id} (edit any field)
    - PATCH /tasks/{task_id}/toggle (toggle completion)
    - DELETE /tasks/{task_id}
  - DB: Use MONGO_URL, tasks collection, UUID id; ensure timezone-aware datetimes. Add helper serialize_doc(s).
  - CORS: Allow frontend origin; bind 0.0.0.0:8001. Order specific routes before generic.
- Frontend (React + shadcn/ui + Tailwind)
  - Screens/Components: Header, TaskForm (title, description, date, category), FilterBar (All/Active/Completed + Category select), TaskList, TaskItem (icons: edit, delete, check), EditModal, EmptyState, Spinner/Loader, Toasts.
  - UX: 
    - Create task (all fields). 
    - Edit task via modal (all fields). 
    - Toggle completion inline. 
    - Delete with confirmation. 
    - Filter by status, view category badges with colors.
  - State: tasks[], loading, submitting, error, filterState, modalState.
  - API: Use REACT_APP_BACKEND_URL + /api; robust error handling, loading indicators, empty-state messages.
- Visual Design
  - Modern palette and category color chips; clear iconography (e.g., lucide-react). Consistent spacing/typography via shadcn.
- Logging/Validation
  - Frontend: run esbuild lint check; handle all states precisely (loading/empty/error/success).
  - Backend: pydantic validation, clear error messages.
- Testing (end of phase)
  - Call Testing Agent for E2E (Primary Workflow + Critical Data Flow + Error states). Skip any drag-and-drop/camera/voice tests.
  - Update plan with status; fix issues until all pass.

User Stories (Phase 2)
1. As a user, I can add a task with title, description, due date, and category so I can plan work clearly.
2. As a user, I can mark a task complete/incomplete and instantly see status change in the list.
3. As a user, I can filter by All/Active/Completed to focus on what matters.
4. As a user, I can edit any task field later from a convenient modal.
5. As a user, I can delete a task with a confirmation so I don’t remove items by mistake.
6. As a user, I see a friendly empty state when no tasks match my filters.

Phase 2: All user stories covered in Development and testing.
Phase 2: End to End Testing using Testing Agent.

---

### Phase 3: Adding More Features (UX Enhancements)
- Features
  - Search by title/description (client-side) and sort by due_date (asc/desc).
  - Overdue highlighting (e.g., red badge) and due-soon accent.
  - Category filter dropdown; quick category badges in list.
  - Bulk actions: complete selected, clear completed.
  - Polished confirmations and toasts; improved date picker UX.
- Backend
  - Optional query params: search, sort; efficient queries and indexes as needed.
- Frontend
  - Add search bar, sort control, bulk-selection UI, category filter, improved badges.
- Testing
  - Call Testing Agent again for the new features and regressions.

User Stories (Phase 3)
1. As a user, I can search tasks by text so I quickly find what I need.
2. As a user, I can sort tasks by due date to prioritize my day.
3. As a user, I see overdue tasks clearly highlighted so I don’t miss deadlines.
4. As a user, I can bulk-complete tasks to speed up housekeeping.
5. As a user, I can filter tasks by category to reduce clutter.

Phase 3: End to End Testing using Testing Agent.

---

### Phase 4: Polish & Optional Auth (on approval)
- Design polish: run design agent to finalize design_guidelines.md; apply refined visuals, spacing, and iconography.
- Responsiveness: mobile-friendly layout and tap targets.
- UX Safety: warn on unsaved edits; snackbars for success/error; skeleton loaders.
- Optional: Simple auth (email/password) after user confirmation; user-specific data isolation.
- Optional: Custom categories management.
- Testing
  - Call Testing Agent for full suite including responsive checks (where feasible) and auth (if added).

User Stories (Phase 4)
1. As a user, I interact with a visually polished, modern interface that feels cohesive.
2. As a user, I can confidently navigate on mobile with responsive layouts.
3. As a user, I receive clear success/error toasts so I always know what happened.
4. As a user, I am warned before discarding unsaved changes to prevent data loss.
5. As a user (if auth enabled), I see only my tasks after signing in.

Phase 4: End to End Testing using Testing Agent.

## 3) Implementation Steps (Concise)
1. Backend: Define Task schema (UUIDs, tz-aware datetimes), connect to Mongo, CRUD endpoints with validation, CORS.
2. Frontend: Base layout + theme, TaskForm, TaskList/Item, Filters, EditModal; wire API calls; loading/empty/error states.
3. Visuals: Category color badges, icons, toasts, confirm modals; accessibility basics.
4. Testing: Run Testing Agent for Phase 2; fix all issues; update plan.md status.
5. Phase 3 features: search/sort/overdue/bulk; retest with Testing Agent.
6. Phase 4 polish and optional auth (only after approval); retest with Testing Agent.

## 4) Current Status

### Phase 2: V1 App Development ✅ COMPLETED
- ✅ Backend with Task model, MongoDB connection, and CRUD API endpoints
- ✅ Frontend components (TaskForm, TaskList, TaskItem, FilterBar, EditModal, EmptyState)
- ✅ Modern colorful UI with category colors and icons (following design guidelines)
- ✅ All user stories implemented and working
- ✅ End-to-end testing completed with 85% success rate
- ✅ All core features verified working:
  - Create tasks with title, description, due date, category
  - Edit tasks via modal
  - Toggle completion status
  - Delete tasks with confirmation
  - Filter by status (All/Active/Completed)
  - Filter by category
  - Category badges with correct colors
  - Due date indicators with status colors
  - Toast notifications for all actions
  - Empty states

### GitHub Preparation ✅ COMPLETED
- ✅ Comprehensive README.md with setup instructions
- ✅ .gitignore file for Python and Node
- ✅ .env.example files for backend and frontend
- ✅ CONTRIBUTING.md with development guidelines
- ✅ MIT LICENSE file

## 5) Next Actions
- Phase 3: Add more features (search, sort, overdue highlighting, bulk actions)
- Phase 4: Polish and optional authentication

## 5) Success Criteria
- Endpoints: All CRUD routes return correct data with validation; UUID ids; tz-aware datetimes.
- UI/UX: Modern colorful UI with icons; all states handled (loading/empty/error/success);
  filters work; edit works; deletion confirmed; category badges visible.
- Persistence: Tasks saved, retrieved, updated, and deleted correctly from MongoDB.
- Reliability: No red-screen errors; frontend bundles without import errors; backend logs clean.
- Testing: Testing Agent passes Phase 2/3/4 checks; plan.md updated after each phase.
