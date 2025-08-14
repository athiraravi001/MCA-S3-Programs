package com.example.sumoftwonumbers;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {
    EditText first, second;
    Button add;
    TextView result;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        first = findViewById(R.id.etnum1);
        second = findViewById(R.id.etnum2);
        add = findViewById(R.id.btn);
        result = findViewById(R.id.etsum);
    }

    public void onClick(View view) {
        int n1 = Integer.parseInt(first.getText().toString());
        int n2 = Integer.parseInt(second.getText().toString());
        int sum = n1 + n2;
        result.setText(sum+" ");
    }
}
