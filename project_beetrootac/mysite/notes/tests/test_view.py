from django.test import TestCase
from django.urls import reverse
from notes.models import Note, Category

class NoteIntegrationTests(TestCase):

    def setUp(self):
        self.category = Category.objects.create(title="Work")

    def test_create_note_via_post(self):
        url = reverse('notes:note_create')  # було 'create' → тепер 'note_create'
        data = {
            'title': 'New note',
            'text': 'Some text',
            'category': self.category.id,
            'reminder': ''
        }

        response = self.client.post(url, data)

        self.assertIn(response.status_code, [200, 302])
        self.assertEqual(Note.objects.count(), 1)
        note = Note.objects.first()
        self.assertEqual(note.title, 'New note')

    def test_create_note_invalid_data(self):
        url = reverse('notes:note_create')  # змінили на 'note_create'
        data = {
            'title': '',  # обов'язкове поле порожнє
            'text': 'Text',
            'category': self.category.id
        }

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(Note.objects.count(), 0)
        self.assertContains(response, 'This field is required.')

    def test_edit_note_via_post(self):
        note = Note.objects.create(
            title='Old title',
            text='Old text',
            category=self.category
        )
        url = reverse('notes:note_detail', kwargs={'pk': note.id})  # змінили на 'note_detail'
        data = {
            'title': 'Updated title',
            'text': 'Updated text',
            'category': self.category.id
        }

        response = self.client.post(url, data)
        self.assertIn(response.status_code, [200, 302])

        note.refresh_from_db()
        self.assertEqual(note.title, 'Updated title')
        self.assertEqual(note.text, 'Updated text')

    def test_list_notes(self):
        Note.objects.create(title='Note 1', text='Text 1', category=self.category)
        Note.objects.create(title='Note 2', text='Text 2', category=self.category)

        url = reverse('notes:index')  # змінили на 'index'
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Note 1')
        self.assertContains(response, 'Note 2')
