package kr.co.aiai.app;

import android.annotation.SuppressLint;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity06 extends AppCompatActivity {
    Button btn;
    EditText et_first, et_last, et_disp;

    @SuppressLint("WrongViewCast")
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main06);

        Button btn = findViewById(R.id.btn);
        et_first = findViewById(R.id.et_first);
        et_last = findViewById(R.id.et_last);
        et_disp = findViewById(R.id.et_disp);
        btn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                myClick();
            }
        });
    }
    void myClick(){
        String first = String.valueOf(et_first.getText());
        String last = String.valueOf(et_last.getText());

        int fi = Integer.parseInt(first);
        int la = Integer.parseInt(last);

        String answer = "";
        for(int i = 0; i < la-fi+1; i++){
            for(int j = 0; j < fi+i; j++){
                answer+="*";
            }
            answer+="\n";
        }
        et_disp.setText(answer);
    }

}