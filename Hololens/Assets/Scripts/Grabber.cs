using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.Networking;

public class Grabber : MonoBehaviour
{
    // this address just returns "hello world"
    public static string endpoint = "https://localhost:5000/";

    public string HelloWorld()
    {
        string hW = "Hello World! (from new function)!";
        return hW;
    }

    void Start()
    {
        StartCoroutine(webRequest());
    }

    // make a request to our docker container
    public IEnumerator webRequest()
    {
        using (UnityWebRequest unityWebRequest = UnityWebRequest.Get(endpoint))
        {
            yield return unityWebRequest.SendWebRequest();

            // ensure theres no errors
            if (unityWebRequest.isNetworkError || unityWebRequest.isHttpError)
            {
                print(unityWebRequest.error);
                Debug.Log("error");
            }
            else
            {
                // Show results as text
                Debug.Log("Print from grabber.cs");
                Debug.Log(unityWebRequest.downloadHandler.text);

            }
        }

    }

}
