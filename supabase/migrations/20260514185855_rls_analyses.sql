alter table projets add column user_id uuid;
alter table analyses enable row level security;
create policy "service role full access"
on analyses
for all
to service_role
using (true)
with check (true);

create policy "users see own analyses"
on analyses
for select
to authenticated
using (projet_id in (
    select id from projets
    where user_id = auth.uid()
));