package kr.co.aiai.high;


import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.FileReader;

import android.app.Activity;
import android.content.Context;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

public class ActivityFile extends Activity {
    TextView textview;
    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_file);
        Button btn = findViewById(R.id.btn);
        textview = findViewById(R.id.tv);
        btn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                try {
                    String textWrite = "babo\nbabo\nbabo";
                    FileOutputStream fileoutputstream = openFileOutput("babo.txt", MODE_PRIVATE);
                    fileoutputstream.write(textWrite.getBytes());
                    fileoutputstream.close();
                } catch (Exception e) {
                    e.printStackTrace();
                }
            }
        });


        String textRead = "";

        try {
            BufferedReader bufferedreader = new BufferedReader( new FileReader
                    ("/data/data/kr.or.ddit.app.file/files/babo.txt"));
            String line = "";
            int i = 0;
            while ((line = bufferedreader.readLine()) != null) {
                textRead += i + ":" + line + "₩n";
                i++;
            }
        } catch (Exception e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
        textview.setText(textRead);

    }
}