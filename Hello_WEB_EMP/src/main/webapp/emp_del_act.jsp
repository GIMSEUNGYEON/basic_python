<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<% int cnt = (int)request.getAttribute("cnt"); %>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<script type="text/javascript">
	var cnt = <%=cnt%>;
	if(cnt == 1){
		alert("정상적으로 삭제되었습니다. 리스트로 돌아갑니다.")
		location.href="emp_list";
	}else{
		alert("삭제 실패!")
		history.back();
// 		history.go(-1); //back이랑 같음
	}
</script>
</head>
<body>
</body>
</html>