create type analysis_status as enum (
    'pending',
    'extracting', 
    'ocr_processing',
    'chunking',
    'embedding',
    'analyzing',
    'anonymizing',
    'completed',
    'failed'
);

create table analyses (
    id bigserial primary key,
    projet_id bigint references projets(id),
    status analysis_status default 'pending',
    progress int default 0,
    current_step_message text,
    findings jsonb,
    created_at timestamptz default now(),
    updated_at timestamptz default now()
);