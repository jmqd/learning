select
  {model}s.id as `{model}_id`,
  tag_instances.* 
from
  {model}s 
join
  tag_instances 
on
  {model}s.id = tag_instances.taggable_id 
where
  tag_id in ({tags_array_csv_string})
group by
  {model}s.id
having
  count(*) = {tags_array_count_int}

