package kr.co.aiai.app;

import android.content.Intent;
import android.os.Bundle;
import android.util.Log;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity08 extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main08);

        Log.d("tag", "[MainActivity08] onCreate");

        Intent getIntent = getIntent();

    }

    @Override
    protected void onDestroy() {
        super.onDestroy();
        Log.d("tag", "[MainActivity08] onDestroy");
    }

    @Override
    protected void onStart() {
        super.onStart();
        Log.d("tag", "[MainActivity08] onStart");

    }

    @Override
    protected void onStop() {
        super.onStop();
        Log.d("tag", "[MainActivity08] onStop");

    }

    @Override
    protected void onResume() {
        super.onResume();
        Log.d("tag", "[MainActivity08] onResume");

    }

    @Override
    protected void onPause() {
        super.onPause();
        Log.d("tag", "[MainActivity08] onPause");
    }

    @Override
    protected void onRestart() {
        super.onRestart();
        Log.d("tag", "[MainActivity08] onRestart");

    }
}