from calculator.commands.add_command import AddCommand

def test_add_command():
    command = AddCommand()  # No arguments in constructor
    result = command.execute(2, 3)  # Arguments go in `execute`
    assert result == 5

