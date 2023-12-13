package kr.co.aiai.high;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.webkit.WebView;
import android.webkit.WebViewClient;
import android.widget.Button;
import android.widget.EditText;

public class ActivityWeb extends AppCompatActivity {
    Button btn, btn2;
    WebView wv;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_web);
        EditText et = findViewById(R.id.et_text);
        wv = (WebView) findViewById(R.id.wv);
        btn = findViewById(R.id.btn);
        btn2 = findViewById(R.id.btn2);
        wv.setWebViewClient(new WebViewClient());
        wv.getSettings().setJavaScriptEnabled(true);
        btn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                wv.loadUrl(et.getText().toString());
            }
        });

        btn2.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                String url = "file:///android_asset/index.html";
                wv.loadUrl(url);
            }
        });

    }
}