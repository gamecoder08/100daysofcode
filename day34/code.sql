
-- Leetcode Code: 

SELECT user_id, count(follower_id) as followers_count FROM followers group by user_id order by user_id;