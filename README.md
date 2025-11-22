# project-vidar
domain/
  model/
    Player
    Guard
    Map
    Tile
    Position
    Vector
    PatrolRoute
    VisionCone
  service/
    MovementService
    CollisionService
    VisionService
    GuardAIService

application/
  usecase/
    UpdateGameState


🧪 Liste des features mécaniques à coder en TDD
(par ordre logique)
✅ 1. Position & vecteurs
Tests :
addition
normalisation
distance
angle
✅ 2. Carte (Map) + collisions
Tests :
"le joueur ne peut pas traverser un mur"
"une position est dans une tuile solide / traversable"
✅ 3. Mouvement du joueur
Tests :
déplacement horizontal/vertical
collisions bloquantes
vitesse constante
limite de map
✅ 4. Garde : déplacement sur patrouille
Tests :
suivre une liste de points dans l’ordre
passer au point suivant quand arrivé
boucler la patrouille
✅ 5. Angle de vision
Tests :
joueur dans l’angle = true
joueur hors du cône = false
joueur derrière le garde = false
✅ 6. Raycasting (vision bloquée par murs)
Tests :
mur entre garde et joueur → non vu
aucun mur → vu
joueur trop loin → non vu
✅ 7. États d’IA du garde
4 états :
Patrol
Suspicious
Chase
ReturnToPatrol
Tests :
si joueur détecté → état Chase
si suspicion → se rapproche
si perdu de vue → retour
si calme → reprise patrouille
✅ 8. Détection de bruit (optionnel mais fun)
Tests :
bruit dans rayon → état Suspicious
bruit derrière un mur → ignoré
✅ 9. Règles de victoire/défaite
Tests :
joueur dans sortie → victoire
garde voit joueur → défaite
✅ 10. Boucle d’update du jeu
Use case UpdateGameState :
Tests :
update → mouvement + IA + vision + transitions
ordres d’appel
état final correct