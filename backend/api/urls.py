from django.urls import path

from .views import (
    UserListView,
    PendingPersonnelApprovalsView,
    PersonnelApprovalActionView,
    RegisterView,
    LoginView,
    ActivityListCreateView,
    ActivityDetailView,
    ActivitySubmissionListCreateView,
    ActivitySubmissionDetailView,
    TaskListCreateView,
    TaskDetailView,
    NotificationListView,
    NotificationDetailView,
    MarkAllNotificationsReadView,
    ReportListCreateView,
    ReportDetailView,
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