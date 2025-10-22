package com.example.gridview;

import android.app.AlertDialog;
import android.content.Context;
import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.GridView;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {

    GridView gv;
    String[] gridViewString = {"pic1","pic2","pic3","pic4","pic5","pic6","pic7","pic8"};
    int[] imgarray = {
            R.drawable.pic1, R.drawable.pic2, R.drawable.pic3, R.drawable.pic4,
            R.drawable.pic5, R.drawable.pic6, R.drawable.pic7, R.drawable.pic8
    };

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        gv = findViewById(R.id.gridview);
        ImageAdapter imageAdapter = new ImageAdapter(this, R.layout.grid_item, gridViewString, imgarray);
        gv.setAdapter(imageAdapter);

        gv.setOnItemClickListener(new AdapterView.OnItemClickListener() {
            @Override
            public void onItemClick(AdapterView<?> parent, View view, int position, long id) {
                AlertDialog.Builder bldr = new AlertDialog.Builder(MainActivity.this);
                bldr.setTitle("This is ....");
                AlertDialog alrt = bldr.create();
                alrt.setMessage(gridViewString[position]);
                alrt.show();
            }
        });
    }

    // ===== Inner class ImageAdapter =====
    public class ImageAdapter extends ArrayAdapter {

        private Context mContext;
        private String gvstring[];
        private int imgarray[];
        LayoutInflater inflator = null;

        public ImageAdapter(@NonNull Context c, int resource, String s[], int x[]) {
            super(c, resource);
            mContext = c;
            gvstring = s;
            imgarray = x;
            inflator = LayoutInflater.from(c);
        }

        @Override
        public int getCount() {
            return imgarray.length;
        }

        public Object getItem(int position) {
            return null;
        }

        public View getView(int position, View convertView, ViewGroup parent) {
            if (convertView == null)
                convertView = inflator.inflate(R.layout.grid_item, null);

            TextView image = convertView.findViewById(R.id.tv1);
            ImageView icon = convertView.findViewById(R.id.imgv1);

            icon.setImageResource(imgarray[position]);
            image.setText(gvstring[position]);

            return convertView;
        }
    }
}
