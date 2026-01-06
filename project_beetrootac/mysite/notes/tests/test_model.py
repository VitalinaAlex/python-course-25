from django.test import TestCase
from notes.models import Note, Category

class NoteModelTests(TestCase):

    def setUp(self):
        self.category = Category.objects.create(title="Work")

    def test_create_note_with_valid_data(self):
        note = Note.objects.create(
            title="Test note",
            text="Some text",
            category=self.category
        )

        self.assertEqual(Note.objects.count(), 1)
        self.assertEqual(note.title, "Test note")
        self.assertEqual(note.text, "Some text")
        self.assertEqual(note.category, self.category)

    def test_note_reminder_can_be_null(self):
        note = Note.objects.create(
            title="No reminder",
            text="Text without reminder",
            category=self.category,
            reminder=None
        )

        self.assertIsNone(note.reminder)

    def test_str_returns_title(self):
        note = Note.objects.create(
            title="Readable title",
            text="Text",
            category=self.category
        )

        self.assertEqual(str(note), "Readable title")

# Create your tests here.