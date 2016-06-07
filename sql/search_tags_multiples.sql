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
  tag_id in ({match_all_these_tags})
group by
  {model}s.id
having
  count(*) = {count_of_match_all_these_tags}

