create view vdocente as
select d.id as docente_id, d.legajo, p.apellido, p.nombre, p.dni
from Docente d
inner join Persona p 
	on p.id = d.persona_id;