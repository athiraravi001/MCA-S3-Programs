package com.example.toggleimages;

import android.os.Bundle;
import android.view.View;
import android.widget.ImageView;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {
    ImageView image1, image2;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        image1 = findViewById(R.id.img1);
        image2 = findViewById(R.id.img2);
    }

    public void onClick(View view) {
        if(view==image1)
        {
            image1.setVisibility(View.GONE);
            image2.setVisibility(View.VISIBLE);
        }
        else
        {
            image2.setVisibility(View.GONE);
            image1.setVisibility(View.VISIBLE);
        }
    }
}