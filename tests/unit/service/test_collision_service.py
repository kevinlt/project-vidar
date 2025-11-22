from src.domain.model.map import Map, Tile, TileType
from src.domain.model.position import Position
from src.domain.service.coliision_service import CollisionService
'''
RG-C3 — Collision lors d’un déplacement
    Lorsqu’on veut déplacer une entité d'une Position actuelle à une nouvelle position :
    newPos = pos + vector
    Alors :
    si newPos est traversable → mouvement autorisé
    sinon → mouvement bloqué (l’entité reste à sa position actuelle)
    
RG-C4 — Le moteur ne doit pas autoriser “d’entrer dans un mur”

Important pour TDD :
move(pos, vector) ne doit jamais renvoyer une position dans un mur.

🔶 4. Déplacement avec collisions (pour tests futurs)
RG-C5 — Mouvement partiel NON géré ici
    À ce stade :
    On ne gère pas les collisions “diagonales partiellement bloquées”.
    Si le nouveau point tombe dans un mur → blocage total.
    Le traitement fin (glissement, splitting du vecteur, etc.) viendra plus tard si tu veux.
    
🔶 5. Map et coordonnées réelles
Pour le moteur interne :
RG-M4 — Conversion position réelle → tuile correspondante
    Une position réelle (x, y) corresponde à la tuile :
    tileX = floor(x)
    tileY = floor(y)
    Sauf si tu décides que ta map travaille seulement avec des positions entières (plus simple pour un jeu d’infiltration stylisé).
    
🧪 Checklist TDD — Tests à écrire
Voici une liste claire des tests unitaires à écrire, dans l’ordre :
Tests Map
création de carte vide
accéder à une tuile valide → ok
accéder à une tuile hors limites → OUTSIDE_MAP ou exception
getTile retourne bien le type attendu
Tests Tile
WALL → isSolid = true
FLOOR → isSolid = false
Tests Collision
position sur FLOOR → pas collision
position sur WALL → collision
position hors map → collision
isTraversable retourne false sur un mur
isTraversable retourne false hors map
Tests Mouvement
(Quand tu feras la feature suivante, mais tu peux déjà les préparer)
mouvement vers une tuile FLOOR → position mise à jour
mouvement vers un WALL → bloqué
mouvement qui sort de la carte → bloqué
🎯 Bonus : Option avancée (pour plus tard)
Si tu veux plus tard :
RG-C6 — Vision passe mais déplacement bloqué
Ex : vitre, laser, rideau…
Mais pas nécessaire maintenant.
'''
class TestCollisionService:

    def test_position_is_traversable_if_tile_is_not_solid(self):
        map = Map(10, 10)
        pos = Position(5.2, 5.)
        assert CollisionService.is_traversable(map, pos) == True

    def test_position_is_not_traversable_if_tile_is_solid(self):
        map = Map(10, 10)
        map.set_tile(5,5, Tile(TileType.WALL))
        pos = Position(5.2, 5.)
        assert CollisionService.is_traversable(map, pos) == False

    def test_position_is_not_traversable_if_outside_map(self):
        map = Map(10, 10)
        pos = Position(-1., 5.)
        assert CollisionService.is_traversable(map, pos) == False

    def test_try_to_move_should_gives_new_position_if_succeed(self):
        assert isinstance(CollisionService.try_move(), Position)
