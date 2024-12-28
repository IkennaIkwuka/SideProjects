import unittest
from unittest.mock import patch, mock_open
from cmd.src.main import App

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = App(10, "cmd/docs/Tasks.txt")

    @patch("builtins.open", new_callable=mock_open, read_data="Title:Test\nDescription:Test Description\n")
    def test_init_existing_file(self, _):
        _ = App(10, "cmd/docs/Tasks.txt")
        self.assertEqual(self.app.task_title, ["Test"])
        self.assertEqual(self.app.task_desc, ["Test Description"])

    @patch("builtins.open", new_callable=mock_open)
    def test_init_new_file(self, mock_file):
        mock_file.side_effect = FileNotFoundError
        _ = App(10, "cmd/docs/Tasks.txt")
        mock_file.assert_called_with("cmd/docs/Tasks.txt", "x")

    @patch("builtins.open", new_callable=mock_open)
    def test_add_tasks(self, _):
        with patch("cmd.src.main.utility.ask_for_title_desc", side_effect=["Test Title", "Test Description"]):
            self.app.add_tasks()
            self.assertEqual(self.app.task_title, ["Test Title"])
            self.assertEqual(self.app.task_desc, ["Test Description"])

    @patch("builtins.open", new_callable=mock_open)
    def test_view_tasks(self, _):
        self.app.task_title = ["Test Title"]
        self.app.task_desc = ["Test Description"]
        with patch("builtins.print") as mock_print:
            self.app.view_tasks()
            mock_print.assert_any_call("\n1.\tTitle: Test Title\n\tDescription: Test Description\n")

    @patch("builtins.open", new_callable=mock_open)
    def test_update_tasks(self, _):
        self.app.task_title = ["Old Title"]
        self.app.task_desc = ["Old Description"]
        with patch("cmd.src.main.utility.ask_for_index", return_value=0):
            with patch("cmd.src.main.utility.ask_for_title_desc", side_effect=["New Title", "New Description"]):
                self.app.update_tasks()
                self.assertEqual(self.app.task_title, ["New Title"])
                self.assertEqual(self.app.task_desc, ["New Description"])

    @patch("builtins.open", new_callable=mock_open)
    def test_remove_tasks(self, _):
        self.app.task_title = ["Test Title"]
        self.app.task_desc = ["Test Description"]
        with patch("cmd.src.main.utility.ask_for_index", return_value=0):
            self.app.remove_tasks()
            self.assertEqual(self.app.task_title, [])
            self.assertEqual(self.app.task_desc, [])

    @patch("builtins.open", new_callable=mock_open)
    def test_quit_program(self, mock_file):
        self.app.task_title = ["Test Title"]
        self.app.task_desc = ["Test Description"]
        with patch("builtins.print") as mock_print:
            self.app.quit_program()
            mock_file().write.assert_any_call("Title:Test Title\nDescription:Test Description\n")
            mock_print.assert_any_call("Tasks saved to file, Program ends successfully...")

if __name__ == "__main__":
    unittest.main()