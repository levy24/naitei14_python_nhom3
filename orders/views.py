from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, View
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from myapp.enums import ORDER_STATUS_CHOICES
from myapp.models import Order
from comments.models import Comment

class OrderListView(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'orders/list.html'
    context_object_name = 'orders'

    def get_queryset(self):
        qs = Order.objects.filter(user=self.request.user).order_by('-order_date')
        status = self.request.GET.get('status')

        valid_status = dict(ORDER_STATUS_CHOICES).keys()
        if status in valid_status:
            qs = qs.filter(status=status)
        return qs

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['status_choices'] = ORDER_STATUS_CHOICES
        ctx['current_status'] = self.request.GET.get('status', '')
        return ctx


class OrderDetailView(LoginRequiredMixin, DetailView):
    model = Order
    template_name = 'orders/detail.html'
    context_object_name = 'order'

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        order = self.object

        items = list(order.items.all())         

        product_ids = [it.product_id for it in items]

        user_comments = Comment.objects.filter(
            user=self.request.user,
            product_id__in=product_ids,
        )

        comment_map = {c.product_id: c for c in user_comments}

        for it in items:
            it.user_comment = comment_map.get(it.product_id)

        ctx["items"] = items 
        return ctx

class OrderCancelView(LoginRequiredMixin, View):
    """
    Cho phép user hủy đơn nếu đang ở trạng thái 'pending'
    và đổi sang 'cancelled' (khớp với ORDER_STATUS_CHOICES).
    """

    def post(self, request, pk):
        order = get_object_or_404(Order, pk=pk, user=request.user)

        # chỉ cho hủy khi status = 'pending'
        if order.status != 'pending':
            messages.error(request, 'Đơn hàng này không thể hủy nữa.')
            return redirect('orders:detail', pk=order.pk)

        order.status = 'cancelled'
        order.rejection_reason = 'Người dùng tự hủy đơn.'
        order.save(update_fields=['status', 'rejection_reason', 'updated_at'])

        messages.success(request, 'Đơn hàng đã được hủy thành công.')
        return redirect('orders:detail', pk=order.pk)
