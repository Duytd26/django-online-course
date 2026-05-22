from django.shortcuts import render, get_object_or_404
from .models import Course, Submission

# Bắt buộc có hàm submit
def submit(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    return render(request, 'onlinecourse/exam_result.html', {'course': course})

# Bắt buộc có hàm show_exam_result
def show_exam_result(request, course_id, submission_id):
    course = get_object_or_404(Course, pk=course_id)
    submission = get_object_or_404(Submission, pk=submission_id)
    return render(request, 'onlinecourse/exam_result.html', {'course': course, 'submission': submission})
