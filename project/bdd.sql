
drop table if exists eleves;

create table eleves(
    id SERIAL primary key,  -- Avec SERIAL, si on ajoute un enregistrement, l'id est automatiquement créée 
    nom text not null,
    prenom text not null,
    age integer
);


insert into eleves(id, nom, prenom, age) 
values
(1, 'Dupont', 'Jean', 16),
(3, 'Durand', 'Pierre', 16),
(4, 'Dufour', 'Paul', 15)
;
