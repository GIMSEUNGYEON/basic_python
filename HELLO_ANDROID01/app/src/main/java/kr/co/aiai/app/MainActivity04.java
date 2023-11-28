package kr.co.aiai.app;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

import java.util.Arrays;

public class MainActivity04 extends AppCompatActivity {
    TextView tv1, tv2, tv3, tv4, tv5, tv6;
    Button btn;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main04);
        tv1 = findViewById(R.id.tv1);
        tv2 = findViewById(R.id.tv2);
        tv3 = findViewById(R.id.tv3);
        tv4 = findViewById(R.id.tv4);
        tv5 = findViewById(R.id.tv5);
        tv6 = findViewById(R.id.tv6);

        btn = findViewById(R.id.btn);

        btn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                myClick();
            }
        });

    }
    void myClick(){
        int[] lotto = new int[6];

        for (int i = 0; i < lotto.length; i++) {
            int num = (int) (Math.random() * 45) + 1;
            lotto[i] = num;
            for (int j = 0; j < i; j++) {
                if (lotto[i] == lotto[j]) {
                    i--;
                    break;
                }
            }
        }
        for(int i = 0; i < lotto.length; i++) {
            for(int j = 0; j < i; j++) {
                if(lotto[i] < lotto[j]) {
                    int tmp = lotto[i];
                    lotto[i] = lotto[j];
                    lotto[j] = tmp;
                }
            }
        }

        tv1.setText(lotto[0] + "");
        tv2.setText(lotto[1] + "");
        tv3.setText(lotto[2] + "");
        tv4.setText(lotto[3] + "");
        tv5.setText(lotto[4] + "");
        tv6.setText(lotto[5] + "");

    }
}