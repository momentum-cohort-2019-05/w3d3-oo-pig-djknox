from pig import Die, Player, Turn

def test_a_die_returns_an_int_between_1_and_6_when_rolled():
    die = Die()
    assert(die.roll() in range(1, 7))

def test_a_player_has_no_score_when_created():
    player = Player()
    assert(player.score == 0)

def test_a_turn_has_no_score_when_started():
    turn = Turn(Player())
    assert(turn.score == 0)