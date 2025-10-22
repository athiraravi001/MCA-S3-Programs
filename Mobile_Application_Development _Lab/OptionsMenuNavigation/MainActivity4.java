package com.example.optionsmenunavigation;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import androidx.appcompat.app.AppCompatActivity;

public class MainActivity4 extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState){
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main4);
        if (getSupportActionBar() != null) {
            getSupportActionBar().hide();
        }
    }

    public void onClick3(View view) {
        Intent i = new Intent(MainActivity4.this, MainActivity.class);
        startActivity(i);
    }
}