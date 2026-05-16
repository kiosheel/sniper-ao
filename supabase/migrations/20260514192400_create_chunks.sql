create table chunks (
    id bigserial primary key,
    analyse_id bigint references analyses(id),
    contenu text,
    embedding vector(1024),
    page int,
    doc_type text
);