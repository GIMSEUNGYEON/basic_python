<%@page import="kr.co.aiai.model.Emp"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<%
	Emp vo = (Emp)request.getAttribute("vo");
%>
<style>
	th {		
		width: 50px;
	}
	
	td {
		width: 50px;
		text-align:center;
	}
	input[type=text] {
		width: 50px;
	}

</style>
<script>
	function fn_mod_act(){
		
		document.frm.submit();
		
	}
</script>
</head>
<body>
<form name="frm" action="emp_add_act" method="post">
	<table border="1px solid black">
		<tr>
			<th>사번</th>
			<td><input type="text" name="e_id">
		</tr>
		
		<tr>
			<th>이름</th>
			<td><input type="text" name="e_name">
		</tr>
		
		<tr>
			<th>성별</th>
			<td><input type="text" name="gen">
		</tr>
		
		<tr>
			<th>주소</th>
			<td><input type="text" name="addr">
		</tr>
		<tr>
			<td colspan="2">
				<input type="button" value="저장" onclick="fn_mod_act()">
			</td>
		</tr>
	</table>
</form>
</body>
</html>
