from django.urls import path

from .views import (
    UserListView,
    PendingPersonnelApprovalsView,
    PersonnelApprovalActionView,
    PersonnelProfileUpdateView,
    RegisterView,
    LoginView,
    ActivityListCreateView,
    ActivityDetailView,
    ActivityArchiveListView,
    ActivityArchiveDetailView,
    ActivityAssignmentRemovalView,
    ActivitySubmissionListCreateView,
    ActivitySubmissionDetailView,
    TaskListCreateView,
    TaskDetailView,
    TaskArchiveListView,
    TaskArchiveDetailView,
    TaskAssignmentRemovalView,
    NotificationListView,
    NotificationDetailView,
    MarkAllNotificationsReadView,
    ReportListCreateView,
    ReportDetailView,
    ReportArchiveListView,
    ReportArchiveDetailView,
    ReportAssignmentRemovalView,
    ReportSubmissionListView,
    ReportSubmissionDetailView,
)


urlpatterns = [

    # =====================================================
    # USERS
    # =====================================================

    path(
        "users/",
        UserListView.as_view(),
        name="user-list"
    ),

    path(
        "users/pending-approvals/",
        PendingPersonnelApprovalsView.as_view(),
        name="pending-approvals"
    ),

    path(
        "users/<int:pk>/approval/",
        PersonnelApprovalActionView.as_view(),
        name="personnel-approval"
    ),

    path(
        "users/<int:pk>/profile/",
        PersonnelProfileUpdateView.as_view(),
        name="personnel-profile-update"
    ),

    # =====================================================
    # AUTH
    # =====================================================

    path(
        "auth/register/",
        RegisterView.as_view(),
        name="register"
    ),

    path(
        "auth/login/",
        LoginView.as_view(),
        name="login"
    ),

    # =====================================================
    # ACTIVITIES
    # =====================================================

    path(
        "activities/",
        ActivityListCreateView.as_view(),
        name="activity-list-create"
    ),

    path(
        "activities/<int:pk>/",
        ActivityDetailView.as_view(),
        name="activity-detail"
    ),

    path(
        "activity-archives/",
        ActivityArchiveListView.as_view(),
        name="activity-archive-list",
    ),

    path(
        "activities/<int:activity_id>/archive/",
        ActivityArchiveDetailView.as_view(),
        name="activity-archive-detail",
    ),

    path(
        "activities/<int:activity_id>/assignment/",
        ActivityAssignmentRemovalView.as_view(),
        name="activity-assignment-removal",
    ),

    # =====================================================
    # ACTIVITY SUBMISSIONS
    # =====================================================

    path(
        "activity-submissions/",
        ActivitySubmissionListCreateView.as_view(),
        name="activity-submission-list-create"
    ),

    path(
        "activity-submissions/<int:pk>/",
        ActivitySubmissionDetailView.as_view(),
        name="activity-submission-detail"
    ),

    path(
        "tasks/",
        TaskListCreateView.as_view(),
        name="task-list-create"
    ),

    path(
        "tasks/<int:pk>/",
        TaskDetailView.as_view(),
        name="task-detail"
    ),

    path(
        "task-archives/",
        TaskArchiveListView.as_view(),
        name="task-archive-list",
    ),

    path(
        "tasks/<int:task_id>/archive/",
        TaskArchiveDetailView.as_view(),
        name="task-archive-detail",
    ),

    path(
        "tasks/<int:task_id>/assignment/",
        TaskAssignmentRemovalView.as_view(),
        name="task-assignment-removal",
    ),

    path(
        "notifications/",
        NotificationListView.as_view(),
        name="notification-list"
    ),

    path(
        "notifications/mark-all-read/",
        MarkAllNotificationsReadView.as_view(),
        name="notification-mark-all-read"
    ),

    path(
        "notifications/<int:pk>/",
        NotificationDetailView.as_view(),
        name="notification-detail"
    ),

    path(
        "reports/",
        ReportListCreateView.as_view(),
        name="report-list-create"
    ),

    path(
        "reports/<int:pk>/",
        ReportDetailView.as_view(),
        name="report-detail"
    ),

    path(
        "report-archives/",
        ReportArchiveListView.as_view(),
        name="report-archive-list",
    ),

    path(
        "reports/<int:report_id>/archive/",
        ReportArchiveDetailView.as_view(),
        name="report-archive-detail",
    ),

    path(
        "report-submissions/<int:submission_id>/assignment/",
        ReportAssignmentRemovalView.as_view(),
        name="report-assignment-removal",
    ),

    path(
        "report-submissions/",
        ReportSubmissionListView.as_view(),
        name="report-submission-list"
    ),

    path(
        "report-submissions/<int:pk>/",
        ReportSubmissionDetailView.as_view(),
        name="report-submission-detail"
    ),
]