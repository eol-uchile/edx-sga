# Generated by Django 2.2.13 on 2020-08-11 16:11

from django.db import migrations
from submissions.models import StudentItem

def fix_submission_types(apps, schema_editor):
    """
    Fix wrongly inserted item_type in submissions, which was default as sga instead of edx_sga, making
    course grade calculations to crash

    Traceback (most recent call last):
    File "/usr/local/lib/python3.5/dist-packages/celery/app/trace.py", line 240, in trace_task
        R = retval = fun(*args, **kwargs)
    File "/usr/local/lib/python3.5/dist-packages/celery/app/trace.py", line 438, in __protected_call__
        return self.run(*args, **kwargs)
    File "/openedx/edx-platform/lms/djangoapps/grades/tasks.py", line 182, in recalculate_subsection_grade_v3
        _recalculate_subsection_grade(self, **kwargs)
    File "/openedx/edx-platform/lms/djangoapps/grades/tasks.py", line 251, in _recalculate_subsection_grade
        raise self.retry(kwargs=kwargs, exc=exc)
    File "/usr/local/lib/python3.5/dist-packages/celery/app/task.py", line 684, in retry
        maybe_reraise()
    File "/usr/local/lib/python3.5/dist-packages/celery/utils/__init__.py", line 248, in maybe_reraise
        reraise(exc_info[0], exc_info[1], exc_info[2])
    File "/usr/local/lib/python3.5/dist-packages/celery/five.py", line 91, in reraise
        raise value
    File "/openedx/edx-platform/lms/djangoapps/grades/tasks.py", line 234, in _recalculate_subsection_grade
        raise DatabaseNotReadyError
    lms.djangoapps.grades.exceptions.DatabaseNotReadyError
    """
    StudentItem.objects.filter(item_type="sga", item_id__contains="type@edx_sga").update(item_type="edx_sga")

def reverse_fix_submission_types(apps, schema_editor):
    StudentItem.objects.filter(item_type="edx_sga", item_id__contains="type@edx_sga").update(item_type="sga")

class Migration(migrations.Migration):
    dependencies = [
        ('submissions', '0005_CreateTeamModel'),
    ]

    operations = [
        migrations.RunPython(fix_submission_types, reverse_fix_submission_types),
    ]