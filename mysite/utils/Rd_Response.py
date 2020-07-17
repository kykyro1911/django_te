from django.http import HttpResponseRedirect
from django.utils.deprecation import MiddlewareMixin
from uauth.models import Users
from stu.models import Countaddstu
 
 
class AuthMiddleware(MiddlewareMixin):
  def process_request(self, request):
    # 統一驗證登入
    # return none 或者 不寫return才會繼續往下執行, 不需要執行
    if request.path == '/test/login/' or request.path == '/test/regist/':
      return None
    ticket = request.COOKIES.get('ticket')
    if not ticket:
      return HttpResponseRedirect('/uauth/login/')
 
    users = Users.objects.filter(u_ticket=ticket)
    if not users:
      return HttpResponseRedirect('/uauth/login/')
# 將user賦值在request請求的user上，以後可以直接判斷user有沒有存在
# 備註，django自帶的有user值
    request.user = users[0]
