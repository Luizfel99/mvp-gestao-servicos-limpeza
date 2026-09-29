cat > core/views.py <<'EOF'
from django.shortcuts import render


def dashboard(request):
    return render(request, "core/dashboard.html")
EOF
