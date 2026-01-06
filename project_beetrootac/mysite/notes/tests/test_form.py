from django.test import TestCase
from notes.forms import NoteForm
from notes.models import Category, Note


class NoteFormTests(TestCase):

    def setUp(self):
        self.category = Category.objects.create(title="Work")

    def test_form_is_valid_with_correct_data(self):
        form_data = {
            'title': 'Test note',
            'text': 'Some text',
            'category': self.category.id,
            'reminder': ''
        }

        form = NoteForm(data=form_data)

        self.assertTrue(form.is_valid())

    def test_form_is_invalid_without_title(self):
        form_data = {
            'title': '',
            'text': 'Some text',
            'category': self.category.id,
        }

        form = NoteForm(data=form_data)

        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors)

    def test_form_is_invalid_without_text(self):
        form_data = {
            'title': 'Test note',
            'text': '',
            'category': self.category.id,
        }

        form = NoteForm(data=form_data)

        self.assertFalse(form.is_valid())
        self.assertIn('text', form.errors)

    def test_form_is_invalid_without_category(self):
        form_data = {
            'title': 'Test note',
            'text': 'Some text',
        }

        form = NoteForm(data=form_data)

        self.assertFalse(form.is_valid())
        self.assertIn('category', form.errors)

    def test_form_can_save_note(self):
        form_data = {
            'title': 'Saved note',
            'text': 'Text',
            'category': self.category.id,
        }

        form = NoteForm(data=form_data)
        self.assertTrue(form.is_valid())

        note = form.save()

        self.assertEqual(Note.objects.count(), 1)
        self.assertEqual(note.title, 'Saved note')
        self.assertEqual(note.category, self.category)

    def test_reminder_is_optional(self):
        form_data = {
            'title': 'No reminder',
            'text': 'Text',
            'category': self.category.id,
            'reminder': ''
        }

        form = NoteForm(data=form_data)

        self.assertTrue(form.is_valid())