#Unittest to run below to check program works

import unittest
from task import TaskManager, Task
from io import StringIO
from unittest.mock import patch

class TestTaskManager(unittest.TestCase):
    def test_add_task(self):
        task_manager = TaskManager()
        task1 = Task(1, "Task 1", "Total tasks left to do", "Pending", "View1", "Delete1")
        task_manager.add_task(task1)
        self.assertEqual(len(task_manager.tasks), 1)
        self.assertEqual(task_manager.tasks[0], task1)

    def test_remove_task(self):
        task_manager = TaskManager()
        task1 = Task(1, "Task 1", "Total tasks left to do", "Pending", "View1", "Delete1")
        task_manager.add_task(task1)
        task_manager.remove_task(1)
        self.assertEqual(len(task_manager.tasks), 0)

    def test_get_task(self):
        task_manager = TaskManager()
        task1 = Task(1, "Task 1", "Total tasks left to do", "Pending", "View1", "Delete1")
        task_manager.add_task(task1)
        retrieved_task = task_manager.get_task(1)
        self.assertEqual(retrieved_task, task1)

    @patch('sys.stdout', new_callable=StringIO)
    def test_display_tasks(self, mock_stdout):
        task_manager = TaskManager()
        task1 = Task(1, "Task 1", "Total tasks left to do", "Pending", "View1", "Delete1")
        task2 = Task(2, "Task 2", "Task can not be done too busy", "Uncompleted", "View2", "Delete2")
        task_manager.add_task(task1)
        task_manager.add_task(task2)

        task_manager.display_tasks()
        output = mock_stdout.getvalue()
        self.assertIn("Task id: 1, Name: Task 1, Description: Total tasks left to do, Status: Pending", output)
        self.assertIn("Task id: 2, Name: Task 2, Description: Task can not be done too busy, Status: Uncompleted", output)

    def test_has_remove_task_method(self):
        task_manager = TaskManager()
        self.assertTrue(hasattr(task_manager, "remove_task"))


if __name__ == '__main__':
    unittest.main()