from django.test import TestCase
from django.contrib.auth import get_user_model
from django.core.files import File
from django.contrib.contenttypes.models import ContentType
from django.core.files.storage import Storage
import mock
from attachments.models import Attachment
from tasks.models import Evidence, Task


class TasksTestCase(TestCase):

    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(username='testuser',
                                             email='test@example.com',
                                             password='secret')
        

    def test_evidence_attachments(self):
        task = Task.objects.create(name='Test task',
                                   creator=self.user)
        self.assertEquals(Task.objects.filter(name='Test task').count(), 1)

        evidence = Evidence.objects.create(task=task)
        self.assertEquals(Evidence.objects.filter(task=task).count(), 1)

        att = Attachment()
        att.creator = self.user

        file_mock = mock.MagicMock(spec=File, name='FileMock')
        file_mock.name = 'test1.jpg'
        storage_mock = mock.MagicMock(spec=Storage, name='StorageMock')
        storage_mock.url = mock.MagicMock(name='url')
        storage_mock.url.return_value = '/tmp/test1.jpg'

        ct = ContentType.objects.get(app_label=evidence._meta.app_label,
                                     model=evidence._meta.model_name)
        att.content_type = ct
        att.object_id = evidence.id
        att.attachment_file = file_mock
        
        with mock.patch('django.core.files.storage.default_storage._wrapped', storage_mock):
            att.save()
        self.assertEquals(Attachment.objects.count(), 1)
        self.assertEquals(att, evidence.attachments.first())
