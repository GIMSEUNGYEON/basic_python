<%@page import="kr.co.aiai.model.Emp"%>
<%@page import="java.util.List"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
	EMP_LIST_JSP<br>
<%=request.getAttribute("이름") %>
<!-- 이렇게 하거나 -->
<%-- <% String a = (String)request.getAttribute("이름"); %> --%>
<%-- <%=a %> --%>
<!-- 이렇게 하거나 -->
${a}<br>
<!-- value값으로 넣어야함 -->
<table border="1px solid black">
<ta>
	<th>사번</th>
	<th>이름</th>
	<th>성별</th>
	<th>주소</th>
</ta>
<tr>

<%
	List<Emp> list = (List<Emp>)request.getAttribute("list");
	

	for(Emp e : list){
// 	for(int i = 0; i < list.size(); i++){
// 	이렇게 쓸거면 list.get(i).getE_id()로 데이터 가져옴
%>
	<td>
		<%=e.getE_id() + "\t"%>
	</td>
	<td>
		<%out.print(e.getE_name() + "\t");%>
	</td>
	<td>
		<%out.print(e.getGen() + "\t");%>
	</td>
	<td>
		<%out.println(e.getAddr() + "<br>");%>
	</td>
</tr>
<%
	}
%>
</table>
</body>
</html>