from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from datetime import timedelta, date
from .models import Habit, HabitLog
from .serializers import HabitSerializer, HabitLogSerializer

class HabitViewSet(viewsets.ModelViewSet):
    serializer_class = HabitSerializer

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=True, methods=["get"])
    def streak(self, request, pk=None):
        habit = self.get_object()
        logs = habit.logs.order_by("-date").values_list("date", flat=True)

        streak, longest = 0, 0
        today = date.today()

        for d in logs:
            if d == today - timedelta(days=streak):
                streak += 1
                longest = max(longest, streak)
            else:
                break

        consistency = (
            (len(logs) / ((today - habit.created_at.date()).days + 1)) * 100
            if logs else 0
        )

        return Response({
            "habit": habit.name,
            "current_streak": streak,
            "longest_streak": longest,
            "consistency_percentage": round(consistency, 2),
            "motivation": "🔥 Keep it up!" if streak > 5 else "💪 You got this!"
        })

class HabitLogViewSet(viewsets.ModelViewSet):
    serializer_class = HabitLogSerializer

    def get_queryset(self):
        return HabitLog.objects.filter(habit__user=self.request.user)
