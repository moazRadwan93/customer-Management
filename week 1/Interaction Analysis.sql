---_____________________________________________________Interaction Analysis_________________________________________________________---


--proc for Agent per interaction 
alter procedure Agent_per_interaction
As
select IA.agent_id ,A.FName+' '+A.LName as Agent_fullname, count(IA.interaction_id) as interaction_per_agent
from interaction_Agent_manger as IA join Agent as A on A.Agent_id = IA.Agent_id
group by IA.agent_id,A.FName,A.LName
order by interaction_per_agent desc

Exec Agent_per_interaction


--proc for Type of interaction 
create procedure Type_of_interaction
as
select interaction_type, count(interaction_id) as NUMofInteraction
from Interaction
group by interaction_type
order by NUMofInteraction desc

Exec Type_of_interaction

--proc for interaction outcome char 


create procedure outcome_per_interaction
As
select interaction_outcome ,COUNT(interaction_id) as outcomePinteraction 
from Interaction
group by interaction_outcome
order by outcomePinteraction desc

Exec outcome_per_interaction


--proc for  how many follow ups
create procedure NumberOfFollowUps
as

select follow_up_required, count(Interaction_id) as NUMofFOllOWReq
from Interaction
group by follow_up_required
order by NUMofFOllOWReq desc

exec NumberOfFollowUps

--proc for interaction channel users
create procedure ChnnerUsed
As
select interaction_channel , count(Interaction_id) as ChannelUsed
from Interaction
group by interaction_channel
order by ChannelUsed desc


exec ChnnerUsed



