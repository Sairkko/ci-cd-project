from ci_cd_project.main import guess_the_word


def test_guess_correct():
    assert guess_the_word("python") is True


def test_guess_incorrect():
    assert guess_the_word("java") is False
