package kr.co.aiai.high;

import android.annotation.SuppressLint;
import android.app.Activity;
import android.content.Context;
import android.graphics.Canvas;
import android.graphics.Color;
import android.graphics.Matrix;
import android.graphics.Paint;
import android.os.Bundle;
import android.view.View;

public class ActivityPaint extends Activity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {

        super.onCreate(savedInstanceState);
        setContentView(new ViewMe(this));
    }
    class ViewMe extends View {
        public ViewMe(Context context) {
            super(context);
        }

        @SuppressLint("DrawAllocation")
        @Override
        protected void onDraw(Canvas canvas) {
            Paint paint = new Paint();
            paint.setColor(Color.RED);
            // paint.setAlpha(125);

//            Matrix matrix = new Matrix();
//            matrix.postRotate(45, 100, 100);
//            canvas.setMatrix(matrix);
            String txt = "Hello Graphic";
            canvas.drawText(txt, 0, txt.length(), 100, 100, paint);

            canvas.drawRect( 20, 20, 40,40, paint );

            canvas.drawCircle(300,300, 30, paint);

            canvas.drawLine(10,100,300,100, createPaint(Color.RED, 5));
            canvas.drawLine(10,150,300,150, createPaint(Color.rgb(255,165,0),5));
            canvas.drawLine(10,200,300,200, createPaint(Color.YELLOW,5));
            canvas.drawLine(10,250,300,250, createPaint(Color.GREEN,5));
            canvas.drawLine(10,300,300,300, createPaint(Color.BLUE,5));
            canvas.drawLine(10,350,300,350, createPaint(Color.CYAN,5));
            canvas.drawLine(10,400,300,400, createPaint(Color.MAGENTA,5));

            super.onDraw(canvas);
        }
        private Paint createPaint(int color, float width) {
            Paint paint = new Paint();
            paint.setColor(color);
            paint.setStrokeWidth(width);
            return paint;
        }
    }
}