package com.example.multiintent;

import android.os.Bundle;
import android.view.View;
import android.content.Intent;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }

    public void onClick1(View view) {
        Intent i=new Intent(MainActivity.this, MainActivity2.class);
        startActivity(i);
    }

    public void onClick2(View view) {
        Intent i=new Intent(MainActivity.this, MainActivity3.class);
        startActivity(i);
    }

    public void onClick3(View view) {
        Intent i=new Intent(MainActivity.this, MainActivity4.class);
        startActivity(i);
    }
}
