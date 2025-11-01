package com.example.studentresultevaluator;

import android.os.Bundle;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity3 extends AppCompatActivity {
    TextView tvResult;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main3);

        tvResult = findViewById(R.id.tvResult);

        float percentage = getIntent().getFloatExtra("percentage", 0);

        if (percentage >= 50)
        {
            tvResult.setText("Result : PASS \n\nPercentage : " + percentage + "%");
        }
        else
        {
            tvResult.setText("Result : FAIL \n\nPercentage : " + percentage + "%");
        }
    }
}