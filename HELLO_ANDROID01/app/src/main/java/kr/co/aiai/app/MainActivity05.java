package kr.co.aiai.app;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity05 extends AppCompatActivity {
    Button [] btns;
    Button btn_call;
    TextView tv;
    String answer = "";
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main05);

        btn_call = findViewById(R.id.btn_call);
        btns = new Button[10];
        for(int i = 0; i < btns.length; i++){
            int buttonId = getResources().getIdentifier("btn" + i, "id", getPackageName());
            btns[i] = findViewById(buttonId);
            btns[i].setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View view) {
                    myClick(view);
                }
            });
        }
        tv = findViewById(R.id.tv);
        btn_call.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                myCall();
            }

        });

    }

    void myClick(View view){
        String text = String.valueOf(tv.getText());

        Button tmp = (Button)view;
        String num = String.valueOf(tmp.getText());

        text+= num;
        answer = text;
        tv.setText(text);

    }

    void myCall(){
        Toast.makeText(getApplicationContext(), answer + "에게 전화를 겁니다...", Toast.LENGTH_SHORT).show();
        tv.setText("");

    }
}