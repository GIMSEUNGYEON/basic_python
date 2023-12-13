package kr.co.aiai.high;

import android.app.Activity;
import android.content.Context;
import android.graphics.Canvas;
import android.graphics.Color;
import android.graphics.Paint;
import android.hardware.SensorListener;
import android.hardware.SensorManager;
import android.os.Bundle;
import android.view.View;
import android.widget.TextView;

public class ActivitySensorManagerPaint extends Activity implements SensorListener {
    ViewMe viewme;
    float[] values = new float[6];
    SensorManager sensormanager;

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        viewme = new ViewMe(this);
        setContentView(viewme);
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
            this.values[0] = values[0];
            this.values[1] = values[1];
            this.values[2] = values[2];
            this.values[3] = values[3];
            this.values[4] = values[4];
            this.values[5] = values[5];
            viewme.invalidate();
        }
    }
    private class ViewMe extends View {

        public ViewMe(Context context) {
            super(context);
        }

        @Override
        protected void onDraw(Canvas canvas) {
            Paint paint = new Paint();
            paint.setColor(Color.RED);
            paint.setStrokeWidth(10);
            canvas.drawLine(500 + 20 * 0, 100 + values[0] * 3, 500 + 20 * 0, 500, paint);
            canvas.drawLine(500 + 20 * 1, 100 + values[1] * 3, 500 + 20 * 1, 500, paint);
            canvas.drawLine(500 + 20 * 2, 100 + values[2] * 3, 500 + 20 * 2, 500, paint);
            canvas.drawLine(500 + 20 * 3, 100 + values[3] * 3, 500 + 20 * 3, 500, paint);
            canvas.drawLine(500 + 20 * 4, 100 + values[4] * 3, 500 + 20 * 4, 500, paint);
            canvas.drawLine(500 + 20 * 5, 100 + values[5] * 3, 500 + 20 * 5, 500, paint);

            paint.setColor(Color.BLUE);
            paint.setTextSize(60);
            canvas.drawText(values[0] + "", 50, 200, paint);
            canvas.drawText(values[1] + "", 50, 200 + 60, paint);
            canvas.drawText(values[2] + "", 50, 200 + 120, paint);
            canvas.drawText(values[3] + "", 50, 200 + 180, paint);
            canvas.drawText(values[4] + "", 50, 200 + 240, paint);
            canvas.drawText(values[5] + "", 50, 200 + 300, paint);

            super.onDraw(canvas);
        }

    }
}