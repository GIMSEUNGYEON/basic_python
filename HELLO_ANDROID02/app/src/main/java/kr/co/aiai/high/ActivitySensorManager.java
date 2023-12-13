package kr.co.aiai.high;

import android.app.Activity;
import android.hardware.SensorListener;
import android.hardware.SensorManager;
import android.os.Bundle;
import android.widget.TextView;

public class ActivitySensorManager extends Activity implements SensorListener {
    TextView tv;
    SensorManager sensormanager;

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_sensor_manager);
        tv = (TextView) findViewById(R.id.tv);
        sensormanager = (SensorManager) getSystemService(SENSOR_SERVICE);

    }

    @Override
    protected void onResume() {
        sensormanager.registerListener(this, SensorManager.SENSOR_ALL);
        super.onResume();
    }

    @Override
    protected void onPause() {
        sensormanager.unregisterListener(this);
        super.onPause();
    }

    @Override
    public void onAccuracyChanged(int sensor, int accuracy) {
        // TODO Auto-generated method stub

    }

    @Override
    public void onSensorChanged(int sensor, float[] values) {
        if (sensor == SensorManager.SENSOR_ORIENTATION) {
            String text = "";
            for (int i = 0; i < values.length; i++) {
                text += "value[" + i + "]:" + values[i] + "\n";
            }
            tv.setText(text);
        }
    }
}